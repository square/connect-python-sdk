import uuid

import squareconnect
from squareconnect.models import CatalogCategory
from squareconnect.models import CatalogDiscount
from squareconnect.models import CatalogItem
from squareconnect.models import CatalogItemModifierListInfo
from squareconnect.models import CatalogItemVariation
from squareconnect.models import CatalogModifier
from squareconnect.models import CatalogModifierList
from squareconnect.models import CatalogObject
from squareconnect.models import CatalogObjectBatch
from squareconnect.models import CatalogQuery
from squareconnect.models import CatalogQueryItemsForTax
from squareconnect.models import CatalogQueryPrefix
from squareconnect.models import CatalogTax
from squareconnect.models import Money
from squareconnect.models import BatchUpsertCatalogObjectsRequest
from squareconnect.models import BatchDeleteCatalogObjectsRequest

class CatalogFixture:
    CLIENT_ID_BEVERAGES = '#Beverages'
    CLIENT_ID_CHOCOLATE = '#Chocolate'
    CLIENT_ID_COFFEE = '#Coffee'
    CLIENT_ID_COFFEE_LARGE = '#LargeCoffee'
    CLIENT_ID_COFFEE_SMALL = '#SmallCoffee'
    CLIENT_ID_DISCOUNT = '#Discount'
    CLIENT_ID_HAZELNUT = '#Hazelnut'
    CLIENT_ID_MILK_SKIM = '#SkimMilk'
    CLIENT_ID_MILK_SOY = '#SoyMilk'
    CLIENT_ID_MILK_WHOLE = '#WholeMilk'
    CLIENT_ID_MILKS = '#Milks'
    CLIENT_ID_SALES_TAX = '#SalesTax'
    CLIENT_ID_SYRUPS = '#Syrups'
    CLIENT_ID_TEA = '#Tea'
    CLIENT_ID_TEA_LARGE = '#LargeTea'
    CLIENT_ID_TEA_SMALL = '#SmallTea'
    CLIENT_ID_VANILLA = '#Vanilla'
    CLIENT_ID_AMOUNT_DISCOUNT = '#AmountDiscount'

    objects_by_client_id = dict()
    test_objects = []

    def __init__(self, api):
        self.api = api
        self.delete_test_catalog()
        self.build_test_catalog()

    def close(self):
        self.delete_test_catalog()


    def coffee_id(self):
        return self.object_id(self.CLIENT_ID_COFFEE)

    def small_coffee_id(self):
        return self.object_id(self.CLIENT_ID_COFFEE_SMALL)

    def large_coffee_id(self):
        return self.object_id(self.CLIENT_ID_COFFEE_LARGE)

    def small_tea_id(self):
        return self.object_id(self.CLIENT_ID_TEA_SMALL)

    def beverages_id(self):
        return self.object_id(self.CLIENT_ID_BEVERAGES)

    def milks_id(self):
        return self.object_id(self.CLIENT_ID_MILKS)

    def soy_milk_id(self):
        return self.object_id(self.CLIENT_ID_MILK_SOY)

    def sales_tax_id(self):
        return self.object_id(self.CLIENT_ID_SALES_TAX)

    def syrups_id(self):
        return self.object_id(self.CLIENT_ID_SYRUPS)

    def amount_discount_id(self):
        return self.object_id(self.CLIENT_ID_AMOUNT_DISCOUNT)


    def delete_test_catalog(self):
        while True:
            res = self.api.list_catalog()
            if res.objects is None:
                break
            ids = set()
            for co in res.objects:
                ids.add(co.id)
            delete_request = BatchDeleteCatalogObjectsRequest()
            delete_request.object_ids = list(ids)
            self.api.batch_delete_catalog_objects(delete_request)


    def object_id(self, client_id):
        return self.objects_by_client_id[client_id]

    def build_beverages(self):
        return CatalogObject(
            type='CATEGORY',
            id=self.CLIENT_ID_BEVERAGES,
            category_data=CatalogCategory(
                name='Beverages',
            )
        )

    def build_milks(self):
        return CatalogObject(
            type = 'MODIFIER_LIST',
            id = self.CLIENT_ID_MILKS,
            modifier_list_data = CatalogModifierList(
                name='Milks',
                modifiers =[
                    CatalogObject(
                        type='MODIFIER',
                        id=self.CLIENT_ID_MILK_WHOLE,
                        modifier_data=CatalogModifier(
                            name='Whole Milk'
                        )
                    ),
                    CatalogObject(
                        type='MODIFIER',
                        id=self.CLIENT_ID_MILK_SKIM,
                        modifier_data=CatalogModifier(
                            name='Skim Milk'
                        )
                    ),
                    CatalogObject(
                        type='MODIFIER',
                        id=self.CLIENT_ID_MILK_SOY,
                        modifier_data=CatalogModifier(
                            name='Soy Milk',
                            price_money=Money(50, 'USD')
                        )
                    )
                ]
            )
        )

    def build_syrups(self):
        return CatalogObject(
            type = 'MODIFIER_LIST',
            id = self.CLIENT_ID_SYRUPS,
            modifier_list_data = CatalogModifierList(
                name='Syrups',
                modifiers =[
                    CatalogObject(
                        type='MODIFIER',
                        id=self.CLIENT_ID_HAZELNUT,
                        modifier_data=CatalogModifier(
                            name='Hazelnut'
                        )
                    ),
                    CatalogObject(
                        type='MODIFIER',
                        id=self.CLIENT_ID_VANILLA,
                        modifier_data=CatalogModifier(
                            name='Vanilla'
                        )
                    ),
                    CatalogObject(
                        type='MODIFIER',
                        id=self.CLIENT_ID_CHOCOLATE,
                        modifier_data=CatalogModifier(
                            name='Chocolate',
                            price_money=Money(50, 'USD')
                        )
                    )
                ]
            )
        )

    def build_coffee(self):
        return CatalogObject(
            type='ITEM',
            id=self.CLIENT_ID_COFFEE,
            present_at_all_locations=True,
            item_data=CatalogItem(
                name='Coffee',
                description='Hot bean juice',
                abbreviation='Co',
                category_id=self.CLIENT_ID_BEVERAGES,
                modifier_list_info=[
                    CatalogItemModifierListInfo(modifier_list_id=self.CLIENT_ID_MILKS)
                ],
                tax_ids=[self.CLIENT_ID_SALES_TAX],
                variations=[
                    CatalogObject(
                        type='ITEM_VARIATION',
                        id=self.CLIENT_ID_COFFEE_SMALL, # do we need this?
                        present_at_all_locations=True,
                        item_variation_data=CatalogItemVariation(
                            item_id=self.CLIENT_ID_COFFEE,
                            name='Small',
                            pricing_type='FIXED_PRICING',
                            price_money=Money(195, 'USD')
                        )
                    ),
                    CatalogObject(
                        type='ITEM_VARIATION',
                        id=self.CLIENT_ID_COFFEE_LARGE, # do we need this?
                        present_at_all_locations=True,
                        item_variation_data=CatalogItemVariation(
                            item_id=self.CLIENT_ID_COFFEE,
                            name='Large',
                            pricing_type='FIXED_PRICING',
                            price_money=Money(250, 'USD')
                        )
                    )
                ]
            )
        )

    def build_tea(self):
        return CatalogObject(
            type='ITEM',
            id=self.CLIENT_ID_TEA,
            present_at_all_locations=True,
            item_data=CatalogItem(
                name='Tea',
                description='Hot leaf juice',
                abbreviation='Re',
                category_id=self.CLIENT_ID_BEVERAGES,
                modifier_list_info=[
                    CatalogItemModifierListInfo(modifier_list_id=self.CLIENT_ID_MILKS)
                ],
                tax_ids=[self.CLIENT_ID_SALES_TAX],
                variations=[
                    CatalogObject(
                        type='ITEM_VARIATION',
                        id=self.CLIENT_ID_TEA_SMALL, # do we need this?
                        present_at_all_locations=True,
                        item_variation_data=CatalogItemVariation(
                            item_id=self.CLIENT_ID_TEA,
                            name='Small',
                            pricing_type='FIXED_PRICING',
                            price_money=Money(150, 'USD')
                        )
                    ),
                    CatalogObject(
                        type='ITEM_VARIATION',
                        id=self.CLIENT_ID_TEA_LARGE, # do we need this?
                        present_at_all_locations=True,
                        item_variation_data=CatalogItemVariation(
                            item_id=self.CLIENT_ID_TEA,
                            name='Large',
                            pricing_type='FIXED_PRICING',
                            price_money=Money(200, 'USD')
                        )
                    )
                ]
            )
        )

    def build_sales_tax(self):
        return CatalogObject(
            type='TAX',
            id=self.CLIENT_ID_SALES_TAX,
            present_at_all_locations=True,
            tax_data=CatalogTax(
                name='Sales Tax',
                calculation_phase='TAX_SUBTOTAL_PHASE',
                inclusion_type='ADDITIVE',
                percentage='5.0',
                applies_to_custom_amounts=True,
                enabled=True
            )
        )

    def build_amount_discount(self):
        return CatalogObject(
            type='DISCOUNT',
            id=self.CLIENT_ID_AMOUNT_DISCOUNT,
            discount_data=CatalogDiscount(
                name='50 cents off',
                amount_money=Money(50, 'USD')
            )
        )

    def objects(self):
        return self.test_objects

    def build_test_catalog(self):
        self.test_objects = [
            self.build_beverages(),
            self.build_milks(),
            self.build_syrups(),
            self.build_coffee(),
            self.build_tea(),
            self.build_sales_tax(),
            self.build_amount_discount()
        ]
        batch = CatalogObjectBatch(self.test_objects)
        batches = [batch]
        req = BatchUpsertCatalogObjectsRequest(str(uuid.uuid4()), batches)
        res = self.api.batch_upsert_catalog_objects(req)
        for m in res.id_mappings:
            self.objects_by_client_id[m.client_object_id] = m.object_id
