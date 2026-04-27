
from django.urls import path
from .import views

urlpatterns = [
    path('admin_home/',views.admin_home),
    path('log_out/',views.log_out),
    path('login/',views.login),
    path('login_post/',views.login_post),

    path('add_district/',views.add_district),
    path('add_district_post/',views.add_district_post),

    path('add_package/',views.add_package),
    path('add_package_post/',views.add_package_post),

    path('allocate_package/',views.allocate_package),
    path('allocate_package_post/',views.allocate_package_post),

    path('edit_district/<id>',views.edit_district),
    path('edit_district_post/',views.edit_district_post),

    path('edit_allocated/<id>',views.edit_allocated),
    path('edit_allocated_post/',views.edit_allocated_post),

    path('edit_package/<id>',views.edit_package),
    path('edit_package_post/',views.edit_package_post),

    path('view_district/',views.view_district),
    path('view_district_post/',views.view_district_post),

    path('view_allocated_package/',views.view_allocated),
    path('view_allocated_package_post/',views.view_allocated_post),

    path('view_package/',views.view_package),
    path('view_package_post/',views.view_package_post),

    path('delete_district_officer/<id>',views.delete_district_officer),

    path('delete_package/<id>',views.delete_package),

    path('delete_allocated_package/<id>',views.delete_allocated_package),

    path('add_councilor/',views.add_councilor),
    path('edit_councilor/<id>',views.edit_councilor),
    path('profile_view/',views.profile_view),
    path('tribe_related_problem/',views.tribe_related_problem),
    path('district_view_allocated_package/',views.district_view_allocated_package),
    path('view_councilors/',views.view_councilors),
    path('district_home/',views.district_home),

    path('add_councilor_post/',views.add_councilor_post),
    path('edit_councilor_post/',views.edit_councilor_post),
    path('tribe_related_problem_post/',views.tribe_related_problem_POST),
    path('view_allocated_package_post/',views.view_allocated_package_POST),
    path('view_councilors_POST/',views.view_councilors_POST),
    path('profile_view/',views.profile_view),
    path('delete_councilor/<id>',views.delete_councilor),
    path('councilor_view_tribes/',views.councilor_view_tribes),
    path('councilor_view_tribes_post/',views.councilor_view_tribes_post),


    path('add_coordinater/',views.add_coordinater),
    path('add_coordinater_post/',views.add_coordinater_post),
    path('edit_coordinater/<id>',views.edit_coordinater),
    path('edit_coordinater_post/',views.edit_coordinater_post),
    path('delete_coordinater/<id>',views.delete_coordinater),
    path('counciler_home/',views.counciler_home),
    path('counciler_view_profile/',views.counciler_view_profile),
    path('view_request/',views.view_request),
    path('view_request_post/',views.view_request_post),
    path('view_service_for_allocated_tribe/',views.view_service_for_allocated_tribe),
    path('view_service_for_allocated_tribe_post/',views.view_service_for_allocated_tribe_post),
    path('councilor_view_tribes/',views.councilor_view_tribes),
    path('view_tribes_post/',views.councilor_view_tribes_post),
    path('view_coordinator/',views.view_coordinator),
    path('view_coordinator_post/',views.view_coordinator_post),
    path('view_report/',views.view_report),
    path('view_report_post',views.view_report_post),


    ##############   flutter     #####################


    path('flutt_login/',views.flutt_login),
    path('view_profile/',views.flutt_view_profile),
    path('add_tribal_families',views.flutt_add_tribal_families),
    path('edit_tribal_families',views.flutt_edit_tribal_families),
    path('view_tribal_families',views.flutt_view_tribal_families),

    path('add_family_members',views.flutt_add_family_members),
    path('edit_family_members',views.flutt_edit_family_members),
    path('view_family_members',views.flutt_view_family_members),
    path('report_problem',views.flutt_report_problem),
    path('supply_the_package',views.flutt_supply_the_package),
    path('add_notification',views.flutt_add_notification),
    path('request_entry_for_service',views.flutt_request_entry_for_service),
    path('service_entry_with_tribes_identity_card_verification',views.flutt_service_entry_with_tribes_identity_card_verification),
    path('flutt_change_password/',views.flutt_change_password),
]
