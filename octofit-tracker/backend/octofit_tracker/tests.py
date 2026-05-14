from django.test import TestCase
from .models import User, Team, Activity, Workout, LeaderboardEntry

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories_burned=300, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username='testuser4', email='test4@example.com', password='testpass')
        workout = Workout.objects.create(user=user, name='Morning Routine', description='Pushups and situps', date='2024-01-02')
        self.assertEqual(workout.name, 'Morning Routine')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create_user(username='testuser5', email='test5@example.com', password='testpass')
        entry = LeaderboardEntry.objects.create(user=user, score=100, rank=1, week='2024-01-07')
        self.assertEqual(entry.rank, 1)
