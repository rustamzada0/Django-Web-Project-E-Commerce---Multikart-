from rest_framework import serializers
from ..models import Variant, Product, Category, Vendor, Image, Option


class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
             "id",
             "title_en",
             "parent",
             "slug"
        )


class GetProductSerializer(serializers.ModelSerializer):
    variant = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "price",
            "title_en",
            "desc_en",
            "video",
            "slug",
            "variant"
        )

    def get_variant(self, obj):
        serializer = GetOffProductVariantSerializer(obj.related_variants.all(), many=True)
        return serializer.data


class GetOffProductVariantSerializer(serializers.ModelSerializer):
    get_absolute_url = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()

    class Meta:
        model = Variant
        fields = (
            "id",
            "title",
            "actual_price",
            "slug",
            "color",
            "get_absolute_url"
        )
        
    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url()
    
    def get_color(self, obj):
        return obj.color.title


class GetOffVariantProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "price",
            "title_en",
            "desc_en",
            "video",
            "slug"
        )


class GetVariantSerializer(serializers.ModelSerializer):
    product = GetOffVariantProductSerializer()
    get_absolute_url = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()


    class Meta:
        model = Variant
        fields = (
            "id",
            "title",
            "actual_price",
            "slug",
            "color",
            "product",
            "get_absolute_url"
        )
        
    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url()
    
    def get_color(self, obj):
        return obj.color.title


class GetImageSerializer(serializers.ModelSerializer):
    variant = GetVariantSerializer()

    class Meta:
            model = Image
            fields = (
                "id",
                "image",
                "variant",
            )