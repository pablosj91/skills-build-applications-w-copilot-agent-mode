from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@banner.com', name='Bruce Banner', team=marvel)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)
        diana = User.objects.create(email='diana@prince.com', name='Diana Prince', team=dc)
        barry = User.objects.create(email='barry@allen.com', name='Barry Allen', team=dc)

        # Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training', suggested_for='Strength')
        w2 = Workout.objects.create(name='Flight Drills', description='Aerobic exercise', suggested_for='Endurance')
        w3 = Workout.objects.create(name='Speed Runs', description='Speed and agility', suggested_for='Speed')

        # Activities
        Activity.objects.create(user=tony, type='Iron Suit Training', duration=60, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Shield Throwing', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Gamma Meditation', duration=30, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Flight', duration=50, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Lasso Practice', duration=40, date=timezone.now().date())
        Activity.objects.create(user=barry, type='Speed Run', duration=35, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=95, rank=2)
        Leaderboard.objects.create(user=steve, score=98, rank=1)
        Leaderboard.objects.create(user=bruce, score=80, rank=4)
        Leaderboard.objects.create(user=clark, score=90, rank=3)
        Leaderboard.objects.create(user=diana, score=85, rank=5)
        Leaderboard.objects.create(user=barry, score=70, rank=6)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
