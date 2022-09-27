from cgitb import text
from tkinter.tix import Form
from turtle import textinput
from django import forms

class create_form(forms.Form):
    title = forms.CharField()
    description = forms.CharField()