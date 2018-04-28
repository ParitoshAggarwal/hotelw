# hotelw
It is an api made in Django==1.11. You can call different links to make the updations in database.. Errors are taken care of i.e. price shouldn't be negative and quantity of any type of rooms should be less than five and more than or equal to zero.

### BULK OPERATION:
For bulk requests url to the api should be of form:
1. localhost/bulk/fromMonth/fromDate/toMonth/toDate/sord/condition/price/quant<br>
2. Where sord is single room or double room- 's' for single 'd' for double<br>
3. Condition 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday', 8: 'weakdays', 9: 'weakends', 10:'alldays',<br>
4. Example: localhost/bulk/july/2/july/13/s/10/1200/2<br>

### Single Updates:
For single updates of prices and quantity of rooms url req to api should be like:
1. single/month/date/sord/quant
2. sprice/month/date/sord/price
3. For example; localhost/single/july/2/d/1 - this will change quantity of room typed doubled to 1 on date 2nd July

### Database:
The database contains data of three months that is July, August, September.
This is the sample data to check the outputs.
