#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked function
def GetHoursWorked():  
    hoursWorked = float(input("Enter hours worked: "))
    return hoursWrkd

#write the GetHourlyRate function
def GetHourlyRate():
    hourlyRate = float(input('Enter hourly rate: '))
    return hourlyRate

# write the GetTaxRate function
def GetTaxRate():
    taxRate = float(input('Enter tax Rate: '))
    return taxRate



def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

    

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empName, f'{hoursWrkd:, .2f}', f'{hourlyRate:, .2f}', f'{grossPay:, .2f}', f'{taxRate:, .1%}', f'{incomeTax:, .2f}', f'{netPay:, .2f')
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formattinghours}
    TotHours += hours
    TotGrossPay += grosspay
    TotTax += taxrate
    TotIncomeTax += incometax
    TotNetPay += netpay
    print(f'Total Number Of Employees: {TotHours}, .2.f')
    print(f'Total Gross Pay: {TotGrossPay}, .2.f')
    print(f'Total Tax: {TotTax, .2.f')
    print(f'Total Net Pay: {TotNetPay}, .2.f')
    # taxrate needs to be formatted as percentage
 

    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hoursworked = GetHoursWorked()
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hourlyRate = GetHourlyRate()
        # write the code to assign to taxrate the return value from GetTaxRate
        taxRate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        # write the code to increment the other total variables with the appropriate values

    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)




