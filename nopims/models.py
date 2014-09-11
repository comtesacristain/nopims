from django.db import models
from datetime import datetime
import xlrd, xlwt, re


# Create your models here.
class Master(models.Model):

    
    COLUMNS={"release_date" : 0, "parent_category" : 1,   "category" : 2,    "activity_name" : 3,    "title" : 4,    "operator" : 5,    "eno": 6,    "staff" : 7,    "copied" : 8,    "staged" : 9,    "attached" : 10}
    NOPTA_FILE = '/Users/michael/Public/nopims/NOPTA_20120101_20140728_OpenFile_Well_List.xlsx'
    NOPTA_SHEET_NAME = "NOPTA-OF-Wells"
    WELLS_ROOT = "/nas/pmd/repos/open/Wells/Regulated"
    
    # Fields
    release_date = models.DateField(null=True)
    parent_category = models.TextField()
    category = models.TextField()
    activity_name = models.TextField()
    title = models.TextField()
    operator = models.TextField()
    eno = models.IntegerField(null=True)
    staff = models.TextField()
    copied = models.TextField()
    staged = models.TextField()
    attached = models.TextField()
    activity =  models.OneToOneField("Activity", primary_key=True)
    

    def check_record(self,r):
        for k,v in self.COLUMNS.items():
            if getattr(self, k) != r[v].value:
                self.change_set.create(attribute = k, old_value = getattr(self, k), new_value = r[v].value, date_recorded = datetime.today())
                setattr(self, k, r[v].value)
                self.save()
                
            #    #self._meta.get_field(k) = r[v]
            #    self.save()
    # from nopims.models import Master;Master.read_nopta()
    
    def build_model(self):
        self.associate_wells()
        state_folder = self.title.split('/')[0].split('-')[0]
        state_folder = re.sub("[0-9]",'',state_folder)
        print state_folder
        
    def associate_wells(self):
        if not hasattr(self,"activity"):
            a=Activity(name=self.activity_name)
            self.activity=a
            self.save()
        else:
            a=self.activity
            a.name = self.activity_name
        a.set_well()
        a.save()

         
    
    @classmethod
    def read_nopta(cls):
        workbook = xlrd.open_workbook(cls.NOPTA_FILE)
        sheet = workbook.sheet_by_name(cls.NOPTA_SHEET_NAME)
        num_rows = sheet.nrows
        i = 1
        while i < num_rows:    
            row = cls.parse_row(sheet.row(i))
            title = row[cls.COLUMNS["title"]].value
            release_date = row[cls.COLUMNS["release_date"]].value
            activity_name = row[cls.COLUMNS["activity_name"]].value
            category = row[cls.COLUMNS["category"]].value
            query_set = cls.objects.filter(release_date = release_date, category = category, activity_name = activity_name, title = title) 
            if not query_set.exists():
                cls.insert_record(row)
            else:
                query_set[0].check_record(row)
            i+=1
            
        
    def write_nopta():
        # Read file first, check that everything in the DB is updated and then write
        return
        

    @classmethod
    def insert_record(cls,row):
        kwargs= {k: row[v].value for k, v in cls.COLUMNS.items()}
        m = Master(**kwargs)
        m.save()
        
        

        
    
    @staticmethod
    def xldate_to_date(d):
        if d:
            return datetime(*xlrd.xldate_as_tuple(d,0)).date()
        else:
            d = None
    
    @classmethod
    def parse_row(cls,r):
        if not r[cls.COLUMNS["eno"]].value:
            r[cls.COLUMNS["eno"]].value = None
        r[cls.COLUMNS["release_date"]].value = cls.xldate_to_date(r[cls.COLUMNS["release_date"]].value) 
        return r 
        
    def __str__(self):              # __unicode__ on Python 2
        return self.activity_name
        

class Change(models.Model):
    master = models.ForeignKey(Master)
    attribute = models.TextField()
    old_value = models.TextField()
    new_value = models.TextField()
    date_recorded  = models.DateTimeField()

class Activity(models.Model):
    name = models.TextField()
    well = models.ForeignKey("Well",null=True)
    
    def set_well(self):
        well_name = self.activity_name_to_well_name
        wells = Well.objects.filter(name = well_name)
        if not wells.exist():
            well=Well(name = well_name)
            well.save()
            self.well = well
            self.save()
        
    def activity_name_to_well_name(self):

        print "ORIG: " + self.name
        
        w = re.match("Montara GI|(\w\D+[ -])*(PER|W|A|B|F|H|M|E)?[0-9][0-9]?",self.name).group() 
        print "PARS: " +w
        #return w
    


class Well(models.Model):
    title = models.ForeignKey("ExplorationTitle", null=True)
    name = models.TextField()


class ExplorationTitle(models.Model):
    name = models.TextField()
    operator = models.ForeignKey("Operator")

class Operator(models.Model):
    name = models.TextField()

class Status(models.Model):
    name = models.TextField()

class Path(models.Model):
    master = models.ForeignKey(Master)
    original_path=models.TextField()
    