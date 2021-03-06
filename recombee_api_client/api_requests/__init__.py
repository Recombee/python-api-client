from recombee_api_client.api_requests.add_item import AddItem
from recombee_api_client.api_requests.delete_item import DeleteItem
from recombee_api_client.api_requests.set_item_values import SetItemValues
from recombee_api_client.api_requests.get_item_values import GetItemValues
from recombee_api_client.api_requests.list_items import ListItems
from recombee_api_client.api_requests.add_item_property import AddItemProperty
from recombee_api_client.api_requests.delete_item_property import DeleteItemProperty
from recombee_api_client.api_requests.get_item_property_info import GetItemPropertyInfo
from recombee_api_client.api_requests.list_item_properties import ListItemProperties
from recombee_api_client.api_requests.add_series import AddSeries
from recombee_api_client.api_requests.delete_series import DeleteSeries
from recombee_api_client.api_requests.list_series import ListSeries
from recombee_api_client.api_requests.list_series_items import ListSeriesItems
from recombee_api_client.api_requests.insert_to_series import InsertToSeries
from recombee_api_client.api_requests.remove_from_series import RemoveFromSeries
from recombee_api_client.api_requests.add_group import AddGroup
from recombee_api_client.api_requests.delete_group import DeleteGroup
from recombee_api_client.api_requests.list_groups import ListGroups
from recombee_api_client.api_requests.list_group_items import ListGroupItems
from recombee_api_client.api_requests.insert_to_group import InsertToGroup
from recombee_api_client.api_requests.remove_from_group import RemoveFromGroup
from recombee_api_client.api_requests.add_user import AddUser
from recombee_api_client.api_requests.delete_user import DeleteUser
from recombee_api_client.api_requests.set_user_values import SetUserValues
from recombee_api_client.api_requests.get_user_values import GetUserValues
from recombee_api_client.api_requests.merge_users import MergeUsers
from recombee_api_client.api_requests.list_users import ListUsers
from recombee_api_client.api_requests.add_user_property import AddUserProperty
from recombee_api_client.api_requests.delete_user_property import DeleteUserProperty
from recombee_api_client.api_requests.get_user_property_info import GetUserPropertyInfo
from recombee_api_client.api_requests.list_user_properties import ListUserProperties
from recombee_api_client.api_requests.add_detail_view import AddDetailView
from recombee_api_client.api_requests.delete_detail_view import DeleteDetailView
from recombee_api_client.api_requests.list_item_detail_views import ListItemDetailViews
from recombee_api_client.api_requests.list_user_detail_views import ListUserDetailViews
from recombee_api_client.api_requests.add_purchase import AddPurchase
from recombee_api_client.api_requests.delete_purchase import DeletePurchase
from recombee_api_client.api_requests.list_item_purchases import ListItemPurchases
from recombee_api_client.api_requests.list_user_purchases import ListUserPurchases
from recombee_api_client.api_requests.add_rating import AddRating
from recombee_api_client.api_requests.delete_rating import DeleteRating
from recombee_api_client.api_requests.list_item_ratings import ListItemRatings
from recombee_api_client.api_requests.list_user_ratings import ListUserRatings
from recombee_api_client.api_requests.add_cart_addition import AddCartAddition
from recombee_api_client.api_requests.delete_cart_addition import DeleteCartAddition
from recombee_api_client.api_requests.list_item_cart_additions import ListItemCartAdditions
from recombee_api_client.api_requests.list_user_cart_additions import ListUserCartAdditions
from recombee_api_client.api_requests.add_bookmark import AddBookmark
from recombee_api_client.api_requests.delete_bookmark import DeleteBookmark
from recombee_api_client.api_requests.list_item_bookmarks import ListItemBookmarks
from recombee_api_client.api_requests.list_user_bookmarks import ListUserBookmarks
from recombee_api_client.api_requests.set_view_portion import SetViewPortion
from recombee_api_client.api_requests.delete_view_portion import DeleteViewPortion
from recombee_api_client.api_requests.list_item_view_portions import ListItemViewPortions
from recombee_api_client.api_requests.list_user_view_portions import ListUserViewPortions
from recombee_api_client.api_requests.recommend_items_to_user import RecommendItemsToUser
from recombee_api_client.api_requests.recommend_items_to_item import RecommendItemsToItem
from recombee_api_client.api_requests.recommend_next_items import RecommendNextItems
from recombee_api_client.api_requests.recommend_users_to_user import RecommendUsersToUser
from recombee_api_client.api_requests.recommend_users_to_item import RecommendUsersToItem
from recombee_api_client.api_requests.search_items import SearchItems
from recombee_api_client.api_requests.user_based_recommendation import UserBasedRecommendation
from recombee_api_client.api_requests.item_based_recommendation import ItemBasedRecommendation
from recombee_api_client.api_requests.reset_database import ResetDatabase
from recombee_api_client.api_requests.batch import Batch
