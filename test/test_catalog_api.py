# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import unittest
import uuid

import squareconnect
from squareconnect.apis.catalog_api import CatalogApi
from squareconnect.models import BatchDeleteCatalogObjectsRequest
from squareconnect.models import BatchRetrieveCatalogObjectsRequest
from squareconnect.models import BatchUpsertCatalogObjectsRequest
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
from squareconnect.models import SearchCatalogObjectsRequest
from squareconnect.models import UpdateItemModifierListsRequest
from squareconnect.models import UpdateItemTaxesRequest
from squareconnect.models import UpsertCatalogObjectRequest
from .utils import APITestCase


class TestCatalogApi(APITestCase):
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

    objects_by_client_id = dict()
    test_objects = []

    def build_beverages(self):
        cat = CatalogCategory()
        cat.name = 'Beverages'
        co = CatalogObject()
        co.type = 'CATEGORY'
        co.id = self.CLIENT_ID_BEVERAGES
        co.category_data = cat
        return co

    def build_milks(self):
        whmm = CatalogModifier()
        whmm.name = 'Whole Milk'
        whm = CatalogObject()
        whm.type = 'MODIFIER'
        whm.id = self.CLIENT_ID_MILK_WHOLE
        whm.modifier_data = whmm

        skmm = CatalogModifier()
        skmm.name = 'Skim Milk'
        skm = CatalogObject()
        skm.type = 'MODIFIER'
        skm.id = self.CLIENT_ID_MILK_SKIM
        skm.modifier_data = skmm

        symm = CatalogModifier()
        symm.name = 'Soy Milk'
        symm.price_money = Money(50, 'USD')
        sym = CatalogObject()
        sym.type = 'MODIFIER'
        sym.id = self.CLIENT_ID_MILK_SOY
        sym.modifier_data = symm

        ml = CatalogModifierList()
        ml.name = 'Milks'
        ml.modifiers = [whm, skm, sym]

        co = CatalogObject()
        co.type = 'MODIFIER_LIST'
        co.id = self.CLIENT_ID_MILKS
        co.modifier_list_data = ml
        return co

    def build_syrups(self):
        hzmm = CatalogModifier()
        hzmm.name = 'Hazelnut'
        hzm = CatalogObject()
        hzm.type = 'MODIFIER'
        hzm.id = self.CLIENT_ID_HAZELNUT
        hzm.modifier_data = hzmm

        vnmm = CatalogModifier()
        vnmm.name = 'Vanilla'
        vnm = CatalogObject()
        vnm.type = 'MODIFIER'
        vnm.id = self.CLIENT_ID_VANILLA
        vnm.modifier_data = vnmm

        chmm = CatalogModifier()
        chmm.name = 'Chocolate'
        chm = CatalogObject()
        chm.type = 'MODIFIER'
        chm.id = self.CLIENT_ID_CHOCOLATE
        chm.modifier_data = chmm

        ml = CatalogModifierList()
        ml.name = 'Syrups'
        ml.modifiers = [hzm, vnm, chm]

        co = CatalogObject()
        co.type = 'MODIFIER_LIST'
        co.id = self.CLIENT_ID_SYRUPS
        co.modifier_list_data = ml
        return co

    def build_coffee(self):
        c = CatalogObject()
        c.type = 'ITEM'
        c.id = self.CLIENT_ID_COFFEE
        c.present_at_all_locations = True

        sciv = CatalogItemVariation()
        sciv.item_id = c.id
        sciv.name = 'Small'
        sciv.pricing_type = 'FIXED_PRICING'
        sciv.price_money = Money(195, 'USD')
        sc = CatalogObject()
        sc.type = 'ITEM_VARIATION'
        sc.id = self.CLIENT_ID_COFFEE_SMALL
        sc.present_at_all_locations = True
        sc.item_variation_data = sciv

        lciv = CatalogItemVariation()
        lciv.item_id = c.id
        lciv.name = 'Large'
        lciv.pricing_type = 'FIXED_PRICING'
        lciv.price_money = Money(250, 'USD')
        lc = CatalogObject()
        lc.type = 'ITEM_VARIATION'
        lc.id = self.CLIENT_ID_COFFEE_LARGE
        lc.present_at_all_locations = True
        lc.item_variation_data = lciv

        cimli = CatalogItemModifierListInfo()
        cimli.modifier_list_id = self.CLIENT_ID_MILKS

        ci = CatalogItem()
        ci.name = 'Coffee'
        ci.description = 'Hot bean juice'
        ci.abbreviation = 'Co'
        ci.category_id = self.CLIENT_ID_BEVERAGES
        ci.modifier_list_info = [cimli]
        ci.tax_ids = [self.CLIENT_ID_SALES_TAX]
        ci.variations = [sc, lc]

        c.item_data = ci
        return c

    def build_tea(self):
        c = CatalogObject()
        c.type = 'ITEM'
        c.id = self.CLIENT_ID_TEA
        c.present_at_all_locations = True

        stiv = CatalogItemVariation()
        stiv.item_id = c.id
        stiv.name = 'Small'
        stiv.pricing_type = 'FIXED_PRICING'
        stiv.price_money = Money(150, 'USD')
        st = CatalogObject()
        st.type = 'ITEM_VARIATION'
        st.id = self.CLIENT_ID_TEA_SMALL
        st.present_at_all_locations = True
        st.item_variation_data = stiv

        ltiv = CatalogItemVariation()
        ltiv.item_id = c.id
        ltiv.name = 'Large'
        ltiv.pricing_type = 'FIXED_PRICING'
        ltiv.price_money = Money(200, 'USD')
        lt = CatalogObject()
        lt.type = 'ITEM_VARIATION'
        lt.id = self.CLIENT_ID_TEA_LARGE
        lt.present_at_all_locations = True
        lt.item_variation_data = ltiv

        cimli = CatalogItemModifierListInfo()
        cimli.modifier_list_id = self.CLIENT_ID_MILKS

        ci = CatalogItem()
        ci.name = 'Tea'
        ci.description = 'Hot leaf juice'
        ci.abbreviation = 'Te'
        ci.category_id = self.CLIENT_ID_BEVERAGES
        ci.modifier_list_info = [cimli]
        ci.tax_ids = [self.CLIENT_ID_SALES_TAX]
        ci.variations = [st, lt]

        c.item_data = ci
        return c

    def build_sales_tax(self):
        co = CatalogObject()
        co.type = 'TAX'
        co.id = self.CLIENT_ID_SALES_TAX
        co.present_at_all_locations = True

        t = CatalogTax()
        t.name = 'Sales Tax'
        t.calculation_phase = 'TAX_SUBTOTAL_PHASE'
        t.inclusion_type = 'ADDITIVE'
        t.percentage = '5.0'
        t.applies_to_custom_amounts = True
        t.enabled = True

        co.tax_data = t
        return co

    def build_test_catalog(self):
        self.test_objects = [
            self.build_beverages(),
            self.build_milks(),
            self.build_syrups(),
            self.build_coffee(),
            self.build_tea(),
            self.build_sales_tax()
        ]
        batch = CatalogObjectBatch(self.test_objects)
        batches = [batch]
        req = BatchUpsertCatalogObjectsRequest(str(uuid.uuid4()), batches)
        res = self.api.batch_upsert_catalog_objects(req)
        self.assertIsNone(res.errors)
        for m in res.id_mappings:
            self.objects_by_client_id[m.client_object_id] = m.object_id

    def delete_test_catalog(self):
        while True:
            res = self.api.list_catalog()
            if res.objects is None:
                break
            ids = set()
            self.assertIsNone(res.errors)
            for co in res.objects:
                ids.add(co.id)
            delete_request = BatchDeleteCatalogObjectsRequest()
            delete_request.object_ids = list(ids)
            self.api.batch_delete_catalog_objects(delete_request)

    def setUp(self):
        account = self.accounts['US-Prod']
        self.api = squareconnect.apis.catalog_api.CatalogApi()
        self.api.api_client.configuration.access_token = account['access_token']
        self.delete_test_catalog()
        self.build_test_catalog()

    def tearDown(self):
        self.delete_test_catalog()

    def test_batch_delete_catalog_objects(self):
        ids = self.objects_by_client_id
        coffee_id = ids[self.CLIENT_ID_COFFEE]
        small_coffee_id = ids[self.CLIENT_ID_COFFEE_SMALL]
        large_coffee_id = ids[self.CLIENT_ID_COFFEE_LARGE]
        small_tea_id = ids[self.CLIENT_ID_TEA_SMALL]

        delete_request = BatchDeleteCatalogObjectsRequest()
        delete_request.object_ids = [coffee_id, small_tea_id]
        response = self.api.batch_delete_catalog_objects(delete_request)
        self.assertIsNone(response.errors)
        self.assertEqual(4, len(response.deleted_object_ids))
        self.assertIn(coffee_id, response.deleted_object_ids)
        self.assertIn(small_coffee_id, response.deleted_object_ids)
        self.assertIn(large_coffee_id, response.deleted_object_ids)
        self.assertIn(small_tea_id, response.deleted_object_ids)

    def test_batch_retrieve_catalog_objects(self):
        ids = self.objects_by_client_id
        coffee_id = ids[self.CLIENT_ID_COFFEE]
        sales_tax_id = ids[self.CLIENT_ID_SALES_TAX]
        beverages_id = ids[self.CLIENT_ID_BEVERAGES]
        milks_id = ids[self.CLIENT_ID_MILKS]

        request = BatchRetrieveCatalogObjectsRequest([coffee_id, sales_tax_id])
        response = self.api.batch_retrieve_catalog_objects(request)

        self.assertEqual(2, len(response.objects))

        coffee = response.objects[0]
        self.assertEqual(coffee.type, 'ITEM')
        self.assertEqual(coffee_id, coffee.id)
        self.assertIsNotNone(coffee.updated_at)
        self.assertNotEqual(coffee.version, 0)
        self.assertFalse(coffee.is_deleted)
        self.assertIsNone(coffee.catalog_v1_ids)
        self.assertTrue(coffee.present_at_all_locations)
        self.assertIsNone(coffee.present_at_location_ids)
        self.assertIsNone(coffee.absent_at_location_ids)

        self.assertEqual('Coffee', coffee.item_data.name)
        self.assertEqual('Hot bean juice', coffee.item_data.description)
        self.assertEqual('Co', coffee.item_data.abbreviation)
        self.assertIsNone(coffee.item_data.label_color)
        self.assertIsNone(coffee.item_data.available_online)
        self.assertIsNone(coffee.item_data.available_for_pickup)
        self.assertIsNone(coffee.item_data.available_electronically)
        self.assertEqual(beverages_id, coffee.item_data.category_id)
        self.assertEqual(1, len(coffee.item_data.tax_ids))
        self.assertEqual(sales_tax_id, coffee.item_data.tax_ids[0])
        self.assertEqual(1, len(coffee.item_data.modifier_list_info))
        mod_list_info = coffee.item_data.modifier_list_info[0]
        self.assertEqual(milks_id, mod_list_info.modifier_list_id)
        self.assertIsNone(mod_list_info.modifier_overrides)
        self.assertIsNone(mod_list_info.min_selected_modifiers)
        self.assertIsNone(mod_list_info.max_selected_modifiers)
        self.assertIsNone(mod_list_info.enabled)
        self.assertIsNone(coffee.item_data.image_url)

        self.assertEqual(2, len(coffee.item_data.variations))

        variation0 = coffee.item_data.variations[0].item_variation_data
        self.assertEqual('Small', variation0.name)
        self.assertEqual('FIXED_PRICING', variation0.pricing_type)
        self.assertEqual(195, variation0.price_money.amount)
        self.assertEqual('USD', variation0.price_money.currency)

        variation1 = coffee.item_data.variations[1].item_variation_data
        self.assertEqual('Large', variation1.name)
        self.assertEqual('FIXED_PRICING', variation1.pricing_type)
        self.assertEqual(250, variation1.price_money.amount)
        self.assertEqual('USD', variation1.price_money.currency)

        self.assertIsNone(coffee.category_data)
        self.assertIsNone(coffee.item_variation_data)
        self.assertIsNone(coffee.tax_data)
        self.assertIsNone(coffee.discount_data)
        self.assertIsNone(coffee.modifier_list_data)
        self.assertIsNone(coffee.modifier_data)

        sales_tax = response.objects[1]
        self.assertEqual('TAX', sales_tax.type)
        self.assertEqual(sales_tax_id, sales_tax.id)
        self.assertEqual('Sales Tax', sales_tax.tax_data.name)

    def test_batch_upsert_catalog_objects(self):
        batches = []
        num_objects = 0
        for batch_num in range(3):
            objects = []
            batch = CatalogObjectBatch(objects)
            batches.append(batch)
            for i in range(100):
                item_id = '#Items-{}-{}'.format(batch_num, i)
                variation_id = '#ItemVariation-{}-{}'.format(batch_num, i)

                item = CatalogObject()
                item.type = 'ITEM'
                item.id = item_id

                item_data = CatalogItem()
                item_data.name = 'Item-{}-{}'.format(batch_num, i)
                item.item_data = item_data

                variation = CatalogObject()
                variation.type = 'VARIATION'
                variation.id = variation_id

                variation_data = CatalogItemVariation()
                variation_data.item_id = item_id
                variation_data.name = 'Regular'
                variation_data.pricing_type = 'VARIABLE_PRICING'
                variation.item_variation_data = variation_data

                objects.append(item)
                num_objects += 1

        req = BatchUpsertCatalogObjectsRequest(str(uuid.uuid4()), batches)
        res = self.api.batch_upsert_catalog_objects(req)
        self.assertIsNone(res.errors)

        self.assertEquals(num_objects, len(res.objects))

    def test_catalog_info(self):
        ci = self.api.catalog_info()
        self.assertIsNone(ci.errors)
        limits = ci.limits
        self.assertEqual(200, limits.batch_delete_max_object_ids)
        self.assertEqual(1000, limits.batch_retrieve_max_object_ids)
        self.assertEqual(1000, limits.batch_upsert_max_objects_per_batch)
        self.assertEqual(10000, limits.batch_upsert_max_total_objects)
        self.assertEqual(1000, limits.search_max_page_limit)
        self.assertEqual(1000, limits.update_item_modifier_lists_max_item_ids)
        self.assertEqual(1000, limits.update_item_modifier_lists_max_modifier_lists_to_disable)
        self.assertEqual(1000, limits.update_item_modifier_lists_max_modifier_lists_to_enable)
        self.assertEqual(1000, limits.update_item_taxes_max_item_ids)
        self.assertEqual(1000, limits.update_item_taxes_max_taxes_to_disable)
        self.assertEqual(1000, limits.update_item_taxes_max_taxes_to_enable)

    def test_delete_catalog_object(self):
        ids = self.objects_by_client_id
        coffee_id = ids[self.CLIENT_ID_COFFEE]
        small_coffee_id = ids[self.CLIENT_ID_COFFEE_SMALL]
        large_coffee_id = ids[self.CLIENT_ID_COFFEE_LARGE]
        res = self.api.delete_catalog_object(coffee_id)

        self.assertEquals(3, len(res.deleted_object_ids))
        self.assertIn(coffee_id, res.deleted_object_ids)
        self.assertIn(small_coffee_id, res.deleted_object_ids)
        self.assertIn(large_coffee_id, res.deleted_object_ids)

    def test_list_catalog(self):
        res = self.api.list_catalog()
        self.assertEqual(len(self.test_objects), len(res.objects))

    def test_retrieve_catalog_object(self):
        ids = self.objects_by_client_id
        coffee_id = ids[self.CLIENT_ID_COFFEE]
        res = self.api.retrieve_catalog_object(coffee_id,
                                               include_related_objects=True)
        self.assertIsNone(res.errors)
        self.assertEquals(coffee_id, res.object.id)
        self.assertEqual(3, len(res.related_objects))

        got_milks = False
        got_sales_tax = False
        got_beverages = False
        for obj in res.related_objects:
            if obj.type == 'MODIFIER_LIST'\
                    and obj.modifier_list_data.name == 'Milks':
                got_milks = True
            elif obj.type == 'TAX'\
                    and obj.tax_data.name == 'Sales Tax':
                got_sales_tax = True
            elif obj.type == 'CATEGORY' \
                    and obj.category_data.name == 'Beverages':
                got_beverages = True

        self.assertTrue(got_milks)
        self.assertTrue(got_sales_tax)
        self.assertTrue(got_beverages)

    def test_search_catalog_objects(self):
        req1 = SearchCatalogObjectsRequest()
        prefix_query = CatalogQueryPrefix()
        prefix_query.attribute_name = 'name'
        prefix_query.attribute_prefix = 'Sm'
        query1 = CatalogQuery()
        query1.prefix_query = prefix_query
        req1.query = query1
        req1.include_deleted_objects = False
        req1.include_related_objects = False

        res1 = self.api.search_catalog_objects(req1)
        self.assertEqual(2, len(res1.objects))
        self.assertEqual('ITEM_VARIATION', res1.objects[0].type)
        self.assertEqual('Small', res1.objects[0].item_variation_data.name)
        self.assertEqual('ITEM_VARIATION', res1.objects[1].type)
        self.assertEqual('Small', res1.objects[1].item_variation_data.name)

        req2 = SearchCatalogObjectsRequest()
        items_for_tax_query = CatalogQueryItemsForTax()
        items_for_tax_query.tax_ids = [self.objects_by_client_id[self.CLIENT_ID_SALES_TAX]]
        query2 = CatalogQuery()
        query2.items_for_tax_query = items_for_tax_query
        req2.query = query2
        req2.include_deleted_objects = False
        req2.include_related_objects = False

        res2 = self.api.search_catalog_objects(req2)
        self.assertEqual(2, len(res2.objects))
        self.assertEqual('ITEM', res2.objects[0].type)
        self.assertEqual('ITEM', res2.objects[1].type)

        got_coffee = False
        got_tea = False
        for obj in res2.objects:
            if obj.item_data.name == 'Coffee':
                got_coffee = True
            elif obj.item_data.name == 'Tea':
                got_tea = True
        self.assertTrue(got_coffee)
        self.assertTrue(got_tea)

    def test_update_item_modifier_lists(self):
        ids = self.objects_by_client_id
        coffee_id = ids[self.CLIENT_ID_COFFEE]
        milks_id = ids[self.CLIENT_ID_MILKS]
        syrups_id = ids[self.CLIENT_ID_SYRUPS]
        res1 = self.api.retrieve_catalog_object(coffee_id,
                                                include_related_objects=False)
        self.assertIsNone(res1.errors)
        self.assertEqual(1, len(res1.object.item_data.modifier_list_info))
        ml_id = res1.object.item_data.modifier_list_info[0].modifier_list_id
        self.assertEquals(milks_id, ml_id)

        req = UpdateItemModifierListsRequest()
        req.item_ids = [coffee_id]
        req.modifier_lists_to_disable = [milks_id]
        req.modifier_lists_to_enable = [syrups_id]
        res_update = self.api.update_item_modifier_lists(req)
        self.assertIsNone(res_update.errors)

        res2 = self.api.retrieve_catalog_object(coffee_id,
                                                include_related_objects=False)
        self.assertIsNone(res2.errors)
        self.assertEqual(1, len(res2.object.item_data.modifier_list_info))
        ml_id = res2.object.item_data.modifier_list_info[0].modifier_list_id
        self.assertEquals(syrups_id, ml_id)

    def test_update_item_taxes(self):
        ids = self.objects_by_client_id
        coffee_id = ids[self.CLIENT_ID_COFFEE]
        sales_tax_id = ids[self.CLIENT_ID_SALES_TAX]
        res1 = self.api.retrieve_catalog_object(coffee_id,
                                                include_related_objects=False)
        self.assertIsNone(res1.errors)
        self.assertEqual(1, len(res1.object.item_data.tax_ids))

        req = UpdateItemTaxesRequest()
        req.item_ids = [coffee_id]
        req.taxes_to_disable = [sales_tax_id]
        res_update = self.api.update_item_taxes(req)
        self.assertIsNone(res_update.errors)

        res2 = self.api.retrieve_catalog_object(coffee_id,
                                                include_related_objects=False)
        self.assertIsNone(res2.errors)
        self.assertIsNone(res2.object.item_data.tax_ids)

    def test_upsert_catalog_object(self):
        obj = CatalogObject()
        obj.type = 'DISCOUNT'
        obj.id = self.CLIENT_ID_DISCOUNT
        discount = CatalogDiscount()
        discount.name = 'Half Off'
        discount.percentage = '50.0'
        obj.discount_data = discount
        req = UpsertCatalogObjectRequest(str(uuid.uuid4()), obj)
        res = self.api.upsert_catalog_object(req)

        self.assertEqual('Half Off', res.catalog_object.discount_data.name)
        self.assertIsNotNone(res.catalog_object.id)
        self.assertIsNotNone(res.catalog_object.updated_at)
        self.assertIsNotNone(res.catalog_object.version)
        self.assertIsNotNone(res.catalog_object.is_deleted)

if __name__ == '__main__':
    unittest.main()
