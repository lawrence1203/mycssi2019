#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
    def __str__(self):
        return "label: %s, balance: %s" % (self.label, self.balance)

    def withdraw(self, draw):
        if draw < 0:
            print("Cannot withdraw negatives")
        elif draw <= self.balance:
            self.balance = self.balance - draw
        else:
            print("insufficient funds")

    def deposit(self, dep):
        #self.balance = self.balance + dep
        if dep < 0:
            print("Cannot withdraw negatives")
        else:
            self.balance = self.balance + dep

    def rename(self, new):
        if new is "":
            print("Invalid Name")
        else:
            self.label = new
