from collections import *



class PersonalJoiner(object):
    @staticmethod
    def join_(*args):
        d={}
        for i in args:
            d.update(i._asdict())
            person=namedtuple('person',d)
            person1=person(**d)#(**d) is used for unpacking the dictonary(d={}) into named tuple
        return person1



PersonalDetails=namedtuple('PersonalDetails',['date_of_birth'])
person_1_details=PersonalDetails( date_of_birth='09-04-1991')

person_features=namedtuple('person_features',['eye_color','IQ_score'])
person_1_features=person_features( eye_color='green eyes',IQ_score=109)
PersonalJoiner.join_(person_1_details, person_1_features)

d=PersonalJoiner()
print(d.join_(person_1_details,person_1_features))


#question Create a class PersonalJoiner without init method. When don't we need an init method? (1.5p)
#Created namedtuple called PersonalDetails with a fieldname date_of_birth. (1p)
#Create a new object person_1_details that is a subclass of Personaldetails, with date_of_birth equal to '09-04-1991'. (2p)
#Create a namedtuple called person_features with two fieldnames -- eye_color and IQ_score. (1p)
#Create an object person_1_features with green eyes and IQ score of 109. (1p)

#Can you print out the namespaces of both  person_1_details and PersonalDetails ? Why/why not? (1p)

#Task : Add a static method join that is able to concatenate any amount of named tuples. Essentialy it has to return (namedtuple) containing details from all records in entry order (6p)

#Example of behaviour:

#print(PersonalJoiner.join(person1_1_details, person1_1_features)) has to result in

#Person(date_of_birth='09-04-1991', eye_color='Green', IQ_score=109) .

#HINT : First load the input arguments to a list using NamedTuple _asdict method and then pass these keys to values to the NamedTuple.


