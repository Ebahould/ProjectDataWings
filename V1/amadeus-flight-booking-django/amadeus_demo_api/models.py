# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Additionalservices(models.Model):
    amount = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    chargeableseatnumber = models.CharField(max_length=50, blank=True, null=True)
    idadditionalservices = models.CharField(primary_key=True, max_length=-1)
    idprices = models.ForeignKey('Prices', models.DO_NOTHING, db_column='idprices', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'additionalservices'


class Aircraftequipment(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    idaircraftequipment = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'aircraftequipment'


class Allotmentdetails(models.Model):
    tourname = models.CharField(max_length=50, blank=True, null=True)
    tourreference = models.CharField(max_length=50, blank=True, null=True)
    idallotmentdetails = models.AutoField(primary_key=True)
    idfaredetailsbysegment = models.ForeignKey('Faredetailsbysegment', models.DO_NOTHING, db_column='idfaredetailsbysegment', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allotmentdetails'


class Arrival(models.Model):
    idarrival = models.TextField(primary_key=True)  # This field type is a guess.
    iatacode = models.TextField(db_column='iataCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    terminal = models.TextField(blank=True, null=True)  # This field type is a guess.
    at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'arrival'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chargeablecheckedbags(models.Model):
    quantity = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    weightunit = models.CharField(max_length=50, blank=True, null=True)
    idchargeablecheckedbags = models.AutoField(primary_key=True)
    idfaredetailsbysegment = models.CharField(max_length=-1, blank=True, null=True)
    idadditionalservices = models.ForeignKey(Additionalservices, models.DO_NOTHING, db_column='idadditionalservices', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chargeablecheckedbags'


class Departure(models.Model):
    ideparture = models.TextField(primary_key=True)  # This field type is a guess.
    iatacode = models.TextField(db_column='iataCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    terminal = models.TextField(blank=True, null=True)  # This field type is a guess.
    at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departure'


class Description(models.Model):
    duration = models.CharField(max_length=50, blank=True, null=True)
    iddescription = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'description'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faredetailsbysegment(models.Model):
    farebasis = models.CharField(max_length=50, blank=True, null=True)
    brandedfare = models.CharField(max_length=50, blank=True, null=True)
    classe = models.CharField(max_length=50, blank=True, null=True)
    isallotment = models.BooleanField(blank=True, null=True)
    slicediceindicator = models.CharField(max_length=50, blank=True, null=True)
    idfaredetailsbysegment = models.ForeignKey('self', models.DO_NOTHING, db_column='idfaredetailsbysegment', primary_key=True)
    idadditionalservices = models.ForeignKey(Additionalservices, models.DO_NOTHING, db_column='idadditionalservices', blank=True, null=True)
    cabin = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.IntegerField(blank=True, null=True)
    idtravelerpricings = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faredetailsbysegment'


class Farerule(models.Model):
    currency = models.CharField(max_length=50, blank=True, null=True)
    idfarerule = models.CharField(primary_key=True, max_length=-1)
    idflightoffers = models.ForeignKey('Flightoffers', models.DO_NOTHING, db_column='idflightoffers', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farerule'


class Fee(models.Model):
    idfee = models.AutoField(primary_key=True)
    idtravelerpricings = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee'


class Flightoffers(models.Model):
    source = models.CharField(max_length=50, blank=True, null=True)
    instantticketingrequired = models.BooleanField(blank=True, null=True)
    disablepricing = models.BooleanField(blank=True, null=True)
    nonhomogeneous = models.BooleanField(blank=True, null=True)
    oneway = models.BooleanField(blank=True, null=True)
    paymentcardrequired = models.BooleanField(blank=True, null=True)
    lastticketingdate = models.CharField(max_length=50, blank=True, null=True)
    numberofbookableseats = models.IntegerField(blank=True, null=True)
    validatingairlinecodes = models.CharField(max_length=50, blank=True, null=True)
    idflightoffers = models.CharField(primary_key=True, max_length=50)
    idprices = models.ForeignKey('Prices', models.DO_NOTHING, db_column='idprices', blank=True, null=True)
    idfarerule = models.ForeignKey(Farerule, models.DO_NOTHING, db_column='idfarerule', blank=True, null=True)
    pricingoptionsfaretype = models.CharField(max_length=50, blank=True, null=True)
    currencyprices = models.CharField(max_length=10, blank=True, null=True)
    grandtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    baseprices = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    totalprices = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    idjson = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flightoffers'


class Includedcheckedbags(models.Model):
    quantity = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    idincludedcheckedbags = models.AutoField(primary_key=True)
    idfaredetailsbysegment = models.ForeignKey(Faredetailsbysegment, models.DO_NOTHING, db_column='idfaredetailsbysegment', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'includedcheckedbags'


class Itineraries(models.Model):
    iditineraries = models.CharField(primary_key=True, max_length=-1)
    idflightoffers = models.ForeignKey(Flightoffers, models.DO_NOTHING, db_column='idflightoffers', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itineraries'


class Operatingflight(models.Model):
    carriercode = models.CharField(max_length=50, blank=True, null=True)
    idoperatingflight = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'operatingflight'


class Price(models.Model):
    currency = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)
    base = models.CharField(max_length=50, blank=True, null=True)
    idprice = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'price'


class Prices(models.Model):
    currency = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)
    base = models.CharField(max_length=50, blank=True, null=True)
    margin = models.CharField(max_length=50, blank=True, null=True)
    grandtotal = models.CharField(max_length=50, blank=True, null=True)
    billingcurrency = models.CharField(max_length=50, blank=True, null=True)
    idprices = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'prices'


class Pricingoptions(models.Model):
    publishedfares = models.BooleanField(blank=True, null=True)
    negotiatedfares = models.BooleanField(blank=True, null=True)
    corporatecodes = models.CharField(max_length=50, blank=True, null=True)
    includedcheckedbags = models.BooleanField(blank=True, null=True)
    idpricingoptions = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'pricingoptions'


class Segments(models.Model):
    carriercode = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    numberofstops = models.IntegerField(blank=True, null=True)
    blacklistedineu = models.BooleanField(blank=True, null=True)
    idsegments = models.CharField(primary_key=True, max_length=-1)
    idarrival = models.ForeignKey(Arrival, models.DO_NOTHING, db_column='idarrival', blank=True, null=True)
    ideparture = models.ForeignKey(Departure, models.DO_NOTHING, db_column='ideparture', blank=True, null=True)
    code = models.TextField(blank=True, null=True)  # This field type is a guess.
    aircraft = models.CharField(max_length=50, blank=True, null=True)
    arrival_at = models.CharField(max_length=50, blank=True, null=True)
    arrival_iatacode = models.CharField(db_column='arrival_iataCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    departureiatacode = models.CharField(max_length=50, blank=True, null=True)
    departureterminal = models.CharField(max_length=50, blank=True, null=True)
    departureat = models.CharField(max_length=50, blank=True, null=True)
    idflightoffers = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segments'


class Tax(models.Model):
    amount = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    idtax = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tax'


class Termandcondition(models.Model):
    circumstance = models.CharField(max_length=50, blank=True, null=True)
    notapplicable = models.BooleanField(blank=True, null=True)
    maxpenaltyamount = models.CharField(max_length=50, blank=True, null=True)
    idtermandcondition = models.AutoField(primary_key=True)
    idfarerule = models.ForeignKey(Farerule, models.DO_NOTHING, db_column='idfarerule', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'termandcondition'


class Travelerpricings(models.Model):
    travelerid = models.CharField(max_length=50, blank=True, null=True)
    fareoption = models.CharField(max_length=50, blank=True, null=True)
    idtravelerpricings = models.CharField(primary_key=True, max_length=-1)
    idflightoffers = models.ForeignKey(Flightoffers, models.DO_NOTHING, db_column='idflightoffers', blank=True, null=True)
    idprice = models.ForeignKey(Price, models.DO_NOTHING, db_column='idprice', blank=True, null=True)
    travelertype = models.CharField(max_length=10, blank=True, null=True)
    pricecurrency = models.CharField(max_length=10, blank=True, null=True)
    totalprice = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    baseprice = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    cabin = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travelerpricings'
