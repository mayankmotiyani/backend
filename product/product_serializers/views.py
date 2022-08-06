from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    OrganizationSerializer,
    OurGoalSerializer,
    ProductPaymentMethodSerializer,
    HeadingAndSubheadingSerializer,
    ProductFunctionalitySerializer,
    AboutProductSerializer,
    ProductSolutionContentSerializer,
    ProductOutComeContentSerializer

)
from product.models import (
    Product,
    Organization,
    OurGoal,
    ProductPaymentMethod,
    HeadingAndSubheading,
    ProductFunctionality,
    AboutProduct,
    ProductSolutionContent,
    ProductSolutionImage,
    ProductOutComeContent,
    ProductOutComeImage
    
)
from rest_framework import (
    status
)

class ProductAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_organization_instance = Organization.objects.all()
            serializer = OrganizationSerializer(get_organization_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class SingleProductAPI(APIView):
    pass


class OurGoalAPI(APIView):
    def get(self, request, product_url, *args, **kwargs):
        try:
            get_our_goal_instance = OurGoal.objects.get(product__slug = product_url)
            serializer = OurGoalSerializer(get_our_goal_instance)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class ProductPaymentMethodAPI(APIView):
    def get(self, request, product_url, *args, **kwargs):
        try:
            get_product_payment_method_instance = ProductPaymentMethod.objects.filter(product__slug = product_url)
            get_heading_and_subheading = list(ProductPaymentMethod.objects.filter().values_list("heading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = ProductPaymentMethodSerializer(get_product_payment_method_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        
class ProductFunctionalityAPI(APIView):
    def get(self, request, product_url, *args, **kwargs):
        try:
            get_product_functionality_instance = ProductFunctionality.objects.filter(product__slug = product_url)
            get_heading_and_subheading = list(ProductFunctionality.objects.filter().values_list("heading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = ProductPaymentMethodSerializer(get_product_functionality_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class AboutProductAPI(APIView):
    def get(self, request, product_url, *args, **kwargs):
        try:
            get_about_product_instance = AboutProduct.objects.get(product__slug = product_url)
            serializer = AboutProductSerializer(get_about_product_instance)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class ProductSolutionContentAPI(APIView):
    def get(self, request, product_url, *args, **kwargs):
        try:
            get_product_instance = Product.objects.get(slug=product_url)
            get_product_solution_content_instance = ProductSolutionContent.objects.filter(product_id=get_product_instance.id)
            get_product_solution_image = ProductSolutionImage.objects.get(product_id=get_product_instance.id)
            serializer = ProductSolutionContentSerializer(get_product_solution_content_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "image":get_product_solution_image.image.url,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class ProductSolutionOutCometAPI(APIView):
    def get(self, request, product_url, *args, **kwargs):
        try:
            get_product_instance = Product.objects.get(slug=product_url)
            get_product_outcome_content_instance = ProductOutComeContent.objects.filter(product_id=get_product_instance.id)
            get_product_outcome_image = ProductOutComeImage.objects.get(product_id=get_product_instance.id)
            serializer = ProductOutComeContentSerializer(get_product_outcome_content_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "image":get_product_outcome_image.image.url,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
    
