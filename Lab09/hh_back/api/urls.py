from django.urls import path
from api.views.views import (
    get_companies,
    get_company,
    get_vacancies,
    get_vacancy,
    top_vacancies,
    get_vacancies_by_company,
)
from api.views.fbv import (
    company_list,
    company_detail,
    company_vacancies,
    vacancy_list,
    vacancy_detail
)
from api.views.cbv import CompanyListAPIView, CompanyDetailAPIView
from api.views.cbv import VacancyListAPIView, VacancyDetailAPIView


urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:pk>/', company_detail),
    path('companies/<int:pk>/vacancies/', company_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:pk>/', vacancy_detail),
    path('vacancies/top_ten/', top_vacancies)

]
