# 28. Authentication System

# Abstract:

# Authentication

# Derived:

# OTPAuth
# GoogleAuth
# FacebookAuth

from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class OTPAuth(Authentication):
    def login(self):
        print("Login using OTP")


class GoogleAuth(Authentication):
    def login(self):
        print("Login using Google Account")


class FacebookAuth(Authentication):
    def login(self):
        print("Login using Facebook Account")


o = OTPAuth()
o.login()

g = GoogleAuth()
g.login()

f = FacebookAuth()
f.login()