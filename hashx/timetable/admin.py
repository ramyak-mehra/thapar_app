# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TimetableBoard, Location, OnlineClass, OfflineClass, Holidays


@admin.register(TimetableBoard)
class TimetableBoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'start_repetion',
        'end_repetition',
        'batch',
        'admin_user',
        'created_date',
        'modified_date',
    )
    list_filter = (
        'start_repetion',
        'end_repetition',
        'batch',
        'admin_user',
        'created_date',
        'modified_date',
    )
    search_fields = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'building',
        'room',
        'floor',
        'published',
        'longitude',
        'latitude',
        'location_url',
    )
    list_filter = ('published',)


@admin.register(OnlineClass)
class OnlineClassAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'timetableboard',
        'created_date',
        'modified_date',
        'course',
        'day',
        'start_time',
        'end_time',
        'published',
        'private',
        'meetingURL',
        'isCompleted',
        'recordingURL',
    )
    list_filter = (
        'timetableboard',
        'created_date',
        'modified_date',
        'course',
        'published',
        'private',
        'isCompleted',
    )


@admin.register(OfflineClass)
class OfflineClassAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'timetableboard',
        'created_date',
        'modified_date',
        'course',
        'day',
        'start_time',
        'end_time',
        'published',
        'private',
        'location',
    )
    list_filter = (
        'timetableboard',
        'created_date',
        'modified_date',
        'course',
        'published',
        'private',
        'location',
    )


@admin.register(Holidays)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_filter = ('date',)
    search_fields = ('name',)
