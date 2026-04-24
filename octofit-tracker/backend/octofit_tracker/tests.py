from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')
    def test_user_create(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(email='batman@dc.com', name='Batman', team=team)
        self.assertEqual(str(user), 'batman@dc.com')
    def test_activity_create(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2024-04-24')
        self.assertEqual(str(activity), 'ironman@marvel.com - run')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=team)
        lb = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(str(lb), 'spiderman@marvel.com - 1')
