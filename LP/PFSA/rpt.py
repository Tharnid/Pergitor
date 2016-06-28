def report( grd_usd, target=sys.stdout ):
    lunch_grd= Decimal('12900')
    bribe_grd= 50000
    cab_usd= Decimal('23.50')

    lunch_usd= (lunch_grd/grd_usd).quantize(PENNY)
    bribe_usd= (bribe_grd/grd_usd).quantize(PENNY)

    receipt_1 = "{0:12s}              {1:6.2f} USD"
    receipt_2 = "{0:12s} {1:8.0f} GRD {2:6.2f} USD"
    print( receipt_2.format("Lunch", lunch_grd, lunch_usd), file=target )
    print( receipt_2.format("Bribe", bribe_grd, bribe_usd), file=target )
    print( receipt_1.format("Cab", cab_usd), file=target )
    print( receipt_1.format("Total", lunch_usd+bribe_usd+cab_usd), file=target )
