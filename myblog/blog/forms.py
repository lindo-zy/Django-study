#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django import forms


class AddFroms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
