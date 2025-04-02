from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    
    # Pet Management
    path('pets/', include('pet_profiles.urls')),
    path('health/', include('pet_health.urls')),
    path('activity/', include('pet_activity.urls')),
    path('personality/', include('pet_personality.urls')),
    path('milestones/', include('pet_milestones.urls')),
    path('insurance/', include('pet_insurance.urls')),
    
    # Services
    path('sitters/', include('sitters.urls')),
    path('vets/', include('veterinarian.urls')),
    path('grooming/', include('grooming.urls')),
    path('training/', include('pet_training.urls')),
    path('daycare/', include('daycare.urls')),
    path('emergency/', include('emergency_support.urls')),
    
    # Community
    path('social/', include('pet_social.urls')),
    path('forums/', include('forums.urls')),
    path('events/', include('events.urls')),
    path('find-my-pet/', include('find_my_pet.urls')),
    path('volunteer/', include('volunteer.urls')),
    path('memorials/', include('memorials.urls')),
    
    # Adoption
    path('adoption/', include('adoption.urls')),
    path('compatibility/', include('compatibility_finder.urls')),
    path('success-stories/', include('success_stories.urls')),
    path('shelters/', include('shelter_management.urls')),
    
    # Marketplace
    path('shop/', include('shop.urls')),
    path('donations/', include('donations.urls')),
    path('subscription/', include('subscription_box.urls')),
    path('accessories/', include('accessories_design.urls')),
    path('exchange/', include('pet_exchange.urls')),
    
    # Resources
    path('guides/', include('pet_care_guides.urls')),
    path('recipes/', include('recipe_sharing.urls')),
    path('tips/', include('training_tips.urls')),
    path('travel/', include('travel_resources.urls')),
    path('faq/', include('faq.urls')),
    
    # Other Core Apps
    path('messages/', include('messaging.urls')),
    path('profiles/', include('profiles.urls')),
]