import json
import pycountry
import phonenumbers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import JsonResponse
from phone_iso3166.country import *
from talk_to_us.models import (
    ContactUS
)

class CountryDailingCodeAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            df_country = pd.read_csv('talk_to_us/country_data/country.csv')
            df_country = df_country[df_country['Dial'].notna()]
            df_country['Dial'] = df_country['Dial'].apply(lambda x : x.replace("-",""))
            df_country.drop_duplicates(subset=['Dial'],inplace=True)
            df_country['Dial'] = df_country['Dial'].apply(lambda x : x.split(",")[0])
            df_country = df_country[['FIFA','Dial']]
            new_row = pd.DataFrame({'FIFA':'IND', 'Dial':'91'},index =[0])
            df_country = pd.concat([new_row, df_country]).reset_index(drop = True)
            df_country.drop_duplicates(subset=['Dial'],inplace=True)
            df_country['Dial'] = df_country['Dial'].apply(lambda x : "+" + x)
            df_country['country_with_dialing_code'] = df_country['FIFA'] + " " + df_country['Dial']
            df_country.dropna(inplace=True)
            df_country = df_country[['country_with_dialing_code','Dial']]
            country_list = list(df_country.to_dict('index').values())
            print(country_list)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":{
                    "country_dialing_code":country_list
                }
            }
            return Response(context)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class ContactUsAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            flag = None
            get_contact_detail = request.POST.get('get_contact_detail')
            get_json = json.loads(get_contact_detail)
            get_country_carrier = phone_country(get_json['dialingCode'])
            check_number = phonenumbers.parse(get_json['contactNumber'], get_country_carrier)
            flag = phonenumbers.is_valid_number(check_number)
            if flag:
                get_country_name = pycountry.countries.get(alpha_2=phone_country(get_json['contactNumber']))
                ContactUS.objects.create(
                    fullName = get_json['fullName'],
                    email = get_json['emailId'],
                    contactNumber = get_json['contactNumber'],
                    countryName = get_country_name.name,
                    projectDescription = get_json['projectDescription'],
                )
                context = {
                    "status":status.HTTP_201_CREATED,
                    "success":True,
                    "response":"Successfully Created!"
                }
                return JsonResponse(context,status=status.HTTP_201_CREATED)
            else:
                context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success":False,
                    "response":"Phone number is not valid!"
                }
                return JsonResponse(context,status=status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return JsonResponse(context,status=status.HTTP_400_BAD_REQUEST)