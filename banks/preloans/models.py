from django.db import models
# Create your models here.
class Preloan(models.Model):
# each class variable represents a database i.e. table field in the model
    Bank_name = models.CharField(max_length=200)
    EIR_CODE = models.CharField(max_length=200)
    
    Cust_name = models.CharField(max_length=200)
    Cust_email = models.CharField(max_length=200)
    Cust_occu = models.CharField(max_length=200)
    Cust_salary = models.IntegerField()
    
    def __str__(self):
        return self.Cust_name + " - " + self.Cust_email
        
class Loan(models.Model):
    Loan_Type = models.CharField(max_length=200)
    Loan_Interest = models.FloatField()
    Duration_in_moths = models.IntegerField()
    Married = models.BooleanField(default=False,null=True,blank=False)
        
    def __str__(self):
        return self.Loan_Type 
              
class Loan_Items(models.Model):
    preloan  = models.ForeignKey(Preloan , on_delete=models.SET_NULL, blank=True,null=True)
    Loan_apply_date = models.DateTimeField(auto_now_add=True)
    Loan_id= models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
        
class Loan_orders(models.Model):
    loan = models.ForeignKey(Loan , on_delete=models.SET_NULL, blank=True,null=True)
    loan_items = models.ForeignKey(Loan_Items , on_delete=models.SET_NULL, blank=True,null=True)
    Loan_Installment = models.IntegerField(default=0, null=True, blank=True)
    Loan_disburse_date=models.DateTimeField(auto_now_add=True)
    
class Customer_Address(models.Model):
   # bank = models.ForeignKey(Bank , on_delete=models.SET_NULL, blank=True,null=True)
   #loan_items = models.ForeignKey(Loan_Items , on_delete=models.SET_NULL, blank=True,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    Irecode = models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address;
