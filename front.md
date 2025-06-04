import React, { useState, useEffect } from 'react';
import { 
  User, 
  Calendar, 
  Activity, 
  Heart, 
  BookOpen, 
  Pill, 
  Bell, 
  Settings, 
  Plus,
  ChevronRight,
  Play,
  Check,
  X,
  Menu,
  Home
} from 'lucide-react';

// Mock Data
const mockUser = {
  id: 1,
  email: "user@example.com",
  nickname: "John",
  gender: 1,
  birth_date: "1990-01-01"
};

const mockPainAreas = [
  { id: 1, name: "Head", x: 50, y: 10, is_right: false },
  { id: 2, name: "Neck", x: 50, y: 20, is_right: false },
  { id: 3, name: "Shoulder", x: 30, y: 30, is_right: false },
  { id: 4, name: "Shoulder", x: 70, y: 30, is_right: true },
  { id: 5, name: "Back", x: 50, y: 40, is_right: false },
  { id: 6, name: "Lower Back", x: 50, y: 55, is_right: false },
];

const mockExercises = [
  { id: 1, title: "Neck Stretches", type: "stretch", tutorial: "Gentle neck movements", has_face: true },
  { id: 2, title: "Shoulder Rolls", type: "mobility", tutorial: "Circular shoulder movements", has_face: false },
  { id: 3, title: "Back Extension", type: "strength", tutorial: "Strengthen back muscles", has_face: true },
];

const mockHabits = [
  { id: 1, name: "Drink 8 glasses of water", category: "Hydration" },
  { id: 2, name: "Take medication on time", category: "Medication" },
  { id: 3, name: "Do morning stretches", category: "Exercise" },
];

// Components
const Navigation = ({ activeTab, setActiveTab, isMobile, setShowMobileMenu }) => {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: Home },
    { id: 'pain', label: 'Pain Tracker', icon: Heart },
    { id: 'exercises', label: 'Exercises', icon: Activity },
    { id: 'habits', label: 'Habits', icon: Check },
    { id: 'content', label: 'Learn', icon: BookOpen },
    { id: 'medications', label: 'Medications', icon: Pill },
    { id: 'profile', label: 'Profile', icon: User },
  ];

  if (isMobile) {
    return (
      <div className="bg-white border-b border-gray-200 px-4 py-3 flex justify-between items-center">
        <h1 className="text-xl font-bold text-gray-800">WellnessApp</h1>
        <button 
          onClick={() => setShowMobileMenu(true)}
          className="p-2 text-gray-600"
        >
          <Menu size={24} />
        </button>
      </div>
    );
  }

  return (
    <nav className="bg-white shadow-sm border-r border-gray-200 w-64 min-h-screen">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-blue-600 mb-8">WellnessApp</h1>
        <ul className="space-y-2">
          {navItems.map(item => {
            const Icon = item.icon;
            return (
              <li key={item.id}>
                <button
                  onClick={() => setActiveTab(item.id)}
                  className={`w-full flex items-center px-4 py-3 rounded-lg text-left transition-colors ${
                    activeTab === item.id 
                      ? 'bg-blue-50 text-blue-700 border-r-2 border-blue-500' 
                      : 'text-gray-600 hover:bg-gray-50'
                  }`}
                >
                  <Icon size={20} className="mr-3" />
                  {item.label}
                </button>
              </li>
            );
          })}
        </ul>
      </div>
    </nav>
  );
};

const MobileMenu = ({ activeTab, setActiveTab, showMenu, setShowMenu }) => {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: Home },
    { id: 'pain', label: 'Pain Tracker', icon: Heart },
    { id: 'exercises', label: 'Exercises', icon: Activity },
    { id: 'habits', label: 'Habits', icon: Check },
    { id: 'content', label: 'Learn', icon: BookOpen },
    { id: 'medications', label: 'Medications', icon: Pill },
    { id: 'profile', label: 'Profile', icon: User },
  ];

  if (!showMenu) return null;

  return (
    <div className="fixed inset-0 z-50 md:hidden">
      <div className="fixed inset-0 bg-black bg-opacity-50" onClick={() => setShowMenu(false)} />
      <div className="fixed left-0 top-0 bottom-0 w-64 bg-white shadow-xl">
        <div className="p-6">
          <div className="flex justify-between items-center mb-8">
            <h1 className="text-2xl font-bold text-blue-600">WellnessApp</h1>
            <button onClick={() => setShowMenu(false)} className="p-2 text-gray-600">
              <X size={24} />
            </button>
          </div>
          <ul className="space-y-2">
            {navItems.map(item => {
              const Icon = item.icon;
              return (
                <li key={item.id}>
                  <button
                    onClick={() => {
                      setActiveTab(item.id);
                      setShowMenu(false);
                    }}
                    className={`w-full flex items-center px-4 py-3 rounded-lg text-left transition-colors ${
                      activeTab === item.id 
                        ? 'bg-blue-50 text-blue-700' 
                        : 'text-gray-600 hover:bg-gray-50'
                    }`}
                  >
                    <Icon size={20} className="mr-3" />
                    {item.label}
                  </button>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    </div>
  );
};

const Dashboard = () => {
  const [todayPain, setTodayPain] = useState(3);
  const [completedExercises, setCompletedExercises] = useState(2);
  const [completedHabits, setCompletedHabits] = useState(1);

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Welcome back, {mockUser.nickname}!</h1>
        <div className="text-sm text-gray-500">
          {new Date().toLocaleDateString('en-US', { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
          })}
        </div>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-gradient-to-r from-blue-500 to-blue-600 p-6 rounded-xl text-white">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-blue-100">Pain Level Today</p>
              <p className="text-3xl font-bold">{todayPain}/10</p>
            </div>
            <Heart size={32} className="text-blue-200" />
          </div>
        </div>

        <div className="bg-gradient-to-r from-green-500 to-green-600 p-6 rounded-xl text-white">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-green-100">Exercises Done</p>
              <p className="text-3xl font-bold">{completedExercises}/3</p>
            </div>
            <Activity size={32} className="text-green-200" />
          </div>
        </div>

        <div className="bg-gradient-to-r from-purple-500 to-purple-600 p-6 rounded-xl text-white">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-purple-100">Habits Completed</p>
              <p className="text-3xl font-bold">{completedHabits}/3</p>
            </div>
            <Check size={32} className="text-purple-200" />
          </div>
        </div>

        <div className="bg-gradient-to-r from-orange-500 to-orange-600 p-6 rounded-xl text-white">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-orange-100">Medications</p>
              <p className="text-3xl font-bold">2/2</p>
            </div>
            <Pill size={32} className="text-orange-200" />
          </div>
        </div>
      </div>

      {/* Today's Tasks */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <Activity className="mr-2 text-green-600" size={24} />
            Today's Exercises
          </h2>
          <div className="space-y-3">
            {mockExercises.slice(0, 3).map(exercise => (
              <div key={exercise.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <div className="flex items-center">
                  <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center mr-3">
                    <Play size={16} className="text-green-600" />
                  </div>
                  <div>
                    <p className="font-medium">{exercise.title}</p>
                    <p className="text-sm text-gray-500">{exercise.type}</p>
                  </div>
                </div>
                <button className="text-green-600 hover:text-green-700">
                  <ChevronRight size={20} />
                </button>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <Check className="mr-2 text-purple-600" size={24} />
            Daily Habits
          </h2>
          <div className="space-y-3">
            {mockHabits.map(habit => (
              <div key={habit.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <div className="flex items-center">
                  <input 
                    type="checkbox" 
                    className="w-5 h-5 text-purple-600 rounded mr-3"
                    defaultChecked={habit.id === 1}
                  />
                  <div>
                    <p className="font-medium">{habit.name}</p>
                    <p className="text-sm text-gray-500">{habit.category}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

const PainTracker = () => {
  const [selectedAreas, setSelectedAreas] = useState([]);
  const [painLevel, setPainLevel] = useState(0);
  const [painNote, setPainNote] = useState('');

  const toggleArea = (areaId) => {
    setSelectedAreas(prev => 
      prev.includes(areaId) 
        ? prev.filter(id => id !== areaId)
        : [...prev, areaId]
    );
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Pain Tracker</h1>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Body Map */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-xl font-semibold mb-4">Select Pain Areas</h2>
          <div className="relative w-full max-w-sm mx-auto">
            <svg viewBox="0 0 100 100" className="w-full h-80 border rounded-lg bg-gray-50">
              {/* Simple body outline */}
              <ellipse cx="50" cy="15" rx="8" ry="10" fill="#e5e7eb" stroke="#9ca3af" strokeWidth="1"/>
              <rect x="45" y="25" width="10" height="15" fill="#e5e7eb" stroke="#9ca3af" strokeWidth="1"/>
              <rect x="35" y="30" width="8" height="25" fill="#e5e7eb" stroke="#9ca3af" strokeWidth="1"/>
              <rect x="57" y="30" width="8" height="25" fill="#e5e7eb" stroke="#9ca3af" strokeWidth="1"/>
              <rect x="40" y="40" width="20" height="25" fill="#e5e7eb" stroke="#9ca3af" strokeWidth="1"/>
              
              {/* Pain areas */}
              {mockPainAreas.map(area => (
                <circle
                  key={area.id}
                  cx={area.x}
                  cy={area.y}
                  r="4"
                  fill={selectedAreas.includes(area.id) ? "#dc2626" : "#3b82f6"}
                  className="cursor-pointer hover:opacity-75 transition-opacity"
                  onClick={() => toggleArea(area.id)}
                />
              ))}
            </svg>
          </div>
          <p className="text-sm text-gray-500 mt-2 text-center">
            Click on blue dots to mark pain areas
          </p>
        </div>

        {/* Pain Assessment */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-xl font-semibold mb-4">Pain Assessment</h2>
          
          <div className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Pain Level (0-10)
              </label>
              <div className="flex items-center space-x-2">
                {[...Array(11)].map((_, i) => (
                  <button
                    key={i}
                    onClick={() => setPainLevel(i)}
                    className={`w-10 h-10 rounded-full text-sm font-medium transition-colors ${
                      painLevel === i
                        ? 'bg-red-500 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                  >
                    {i}
                  </button>
                ))}
              </div>
              <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>No Pain</span>
                <span>Worst Pain</span>
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Additional Notes
              </label>
              <textarea
                value={painNote}
                onChange={(e) => setPainNote(e.target.value)}
                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                rows="4"
                placeholder="Describe your pain, triggers, or any other relevant information..."
              />
            </div>

            <button className="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium">
              Save Pain Entry
            </button>
          </div>
        </div>
      </div>

      {/* Recent Entries */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Recent Pain Entries</h2>
        <div className="space-y-3">
          {[
            { date: 'Today, 2:30 PM', level: 4, areas: ['Lower Back', 'Neck'] },
            { date: 'Today, 8:00 AM', level: 6, areas: ['Head', 'Shoulders'] },
            { date: 'Yesterday, 6:15 PM', level: 3, areas: ['Back'] },
          ].map((entry, i) => (
            <div key={i} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div>
                <p className="font-medium">{entry.date}</p>
                <p className="text-sm text-gray-500">
                  Areas: {entry.areas.join(', ')}
                </p>
              </div>
              <div className={`px-3 py-1 rounded-full text-sm font-medium ${
                entry.level <= 3 ? 'bg-green-100 text-green-800' :
                entry.level <= 6 ? 'bg-yellow-100 text-yellow-800' :
                'bg-red-100 text-red-800'
              }`}>
                {entry.level}/10
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const Exercises = () => {
  const [selectedExercise, setSelectedExercise] = useState(null);

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Exercise Library</h1>
        <button className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors font-medium">
          Start Workout
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {mockExercises.map(exercise => (
          <div key={exercise.id} className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow">
            <div className="flex items-center justify-between mb-4">
              <div className={`px-3 py-1 rounded-full text-xs font-medium ${
                exercise.type === 'stretch' ? 'bg-blue-100 text-blue-800' :
                exercise.type === 'mobility' ? 'bg-purple-100 text-purple-800' :
                'bg-green-100 text-green-800'
              }`}>
                {exercise.type}
              </div>
              {exercise.has_face && (
                <div className="bg-orange-100 text-orange-800 px-2 py-1 rounded text-xs font-medium">
                  Face Check
                </div>
              )}
            </div>
            
            <h3 className="text-lg font-semibold mb-2">{exercise.title}</h3>
            <p className="text-gray-600 text-sm mb-4">{exercise.tutorial}</p>
            
            <div className="flex space-x-2">
              <button 
                onClick={() => setSelectedExercise(exercise)}
                className="flex-1 bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors font-medium text-sm flex items-center justify-center"
              >
                <Play size={16} className="mr-2" />
                Start
              </button>
              <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <BookOpen size={16} />
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Exercise History */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Recent Activity</h2>
        <div className="space-y-3">
          {[
            { exercise: 'Neck Stretches', date: 'Today, 9:00 AM', duration: '5 mins' },
            { exercise: 'Back Extension', date: 'Yesterday, 6:30 PM', duration: '8 mins' },
            { exercise: 'Shoulder Rolls', date: 'Yesterday, 8:00 AM', duration: '3 mins' },
          ].map((entry, i) => (
            <div key={i} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div>
                <p className="font-medium">{entry.exercise}</p>
                <p className="text-sm text-gray-500">{entry.date}</p>
              </div>
              <div className="text-sm text-gray-600">
                {entry.duration}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const Habits = () => {
  const [habits, setHabits] = useState(mockHabits.map(h => ({...h, completed: false})));

  const toggleHabit = (id) => {
    setHabits(prev => prev.map(h => 
      h.id === id ? {...h, completed: !h.completed} : h
    ));
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Daily Habits</h1>
        <button className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition-colors font-medium flex items-center">
          <Plus size={16} className="mr-2" />
          Add Habit
        </button>
      </div>

      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Today's Habits</h2>
        <div className="space-y-4">
          {habits.map(habit => (
            <div key={habit.id} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center">
                <input
                  type="checkbox"
                  checked={habit.completed}
                  onChange={() => toggleHabit(habit.id)}
                  className="w-5 h-5 text-purple-600 rounded mr-4"
                />
                <div>
                  <p className={`font-medium ${habit.completed ? 'line-through text-gray-500' : ''}`}>
                    {habit.name}
                  </p>
                  <p className="text-sm text-gray-500">{habit.category}</p>
                </div>
              </div>
              {habit.completed && (
                <div className="text-green-600">
                  <Check size={20} />
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Habit Statistics */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 text-center">
          <div className="text-3xl font-bold text-purple-600 mb-2">
            {habits.filter(h => h.completed).length}/{habits.length}
          </div>
          <p className="text-gray-600">Today's Progress</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 text-center">
          <div className="text-3xl font-bold text-green-600 mb-2">7</div>
          <p className="text-gray-600">Day Streak</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 text-center">
          <div className="text-3xl font-bold text-blue-600 mb-2">85%</div>
          <p className="text-gray-600">Weekly Average</p>
        </div>
      </div>
    </div>
  );
};

const Content = () => {
  const articles = [
    { id: 1, title: "Understanding Chronic Pain", category: "Education", readTime: "5 min" },
    { id: 2, title: "Nutrition for Pain Management", category: "Nutrition", readTime: "8 min" },
    { id: 3, title: "Sleep and Recovery", category: "Wellness", readTime: "6 min" },
  ];

  const videos = [
    { id: 1, title: "Introduction to Pain Science", duration: "12:34" },
    { id: 2, title: "Breathing Techniques for Relaxation", duration: "8:15" },
    { id: 3, title: "Posture and Pain Prevention", duration: "15:22" },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Learn & Discover</h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Articles */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <BookOpen className="mr-2 text-blue-600" size={24} />
            Articles
          </h2>
          <div className="space-y-4">
            {articles.map(article => (
              <div key={article.id} className="p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer">
                <div className="flex justify-between items-start mb-2">
                  <h3 className="font-medium">{article.title}</h3>
                  <span className="text-xs text-gray-500">{article.readTime}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-blue-600 bg-blue-100 px-2 py-1 rounded">
                    {article.category}
                  </span>
                  <ChevronRight size={16} className="text-gray-400" />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Videos */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <Play className="mr-2 text-green-600" size={24} />
            Educational Videos
          </h2>
          <div className="space-y-4">
            {videos.map(video => (
              <div key={video.id} className="p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer">
                <div className="flex justify-between items-start mb-2">
                  <h3 className="font-medium">{video.title}</h3>
                  <span className="text-xs text-gray-500">{video.duration}</span>
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center">
                    <Play size={16} className="text-green-600 mr-2" />
                    <span className="text-sm text-gray-600">Watch now</span>
                  </div>
                  <ChevronRight size={16} className="text-gray-400" />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Meditation Section */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Meditation & Mindfulness</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {[
            { title: "Body Scan Meditation", duration: "10 min", type: "Guided" },
            { title: "Breathing Exercise", duration: "5 min", type: "Focus" },
            { title: "Pain Relief Visualization", duration: "15 min", type: "Healing" },
          ].map((meditation, i) => (
            <div key={i} className="p-4 bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg">
              <h3 className="font-medium mb-2">{meditation.title}</h3>
              <div className="flex justify-between items-center">
                <span className="text-sm text-gray-600">{meditation.duration} • {meditation.type}</span>
                <button className="bg-purple-600 text-white p-2 rounded-full hover:bg-purple-700 transition-colors">
                  <Play size={16} />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const Medications = () => {
  const [medications, setMedications] = useState([
    { id: 1, name: "Ibuprofen", type: "Pain Relief", times: ["8:00 AM", "2:00 PM", "8:00 PM"], taken: [true, false, false] },
    { id: 2, name: "Vitamin D", type: "Supplement", times: ["9:00 AM"], taken: [true] },
  ]);

  const toggleMedication = (medId, timeIndex) => {
    setMedications(prev => prev.map(med => 
      med.id === medId 
        ? {
            ...med, 
            taken: med.taken.map((t, i) => i === timeIndex ? !t : t)
          }
        : med
    ));
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Medications</h1>
        <button className="bg-orange-600 text-white px-4 py-2 rounded-lg hover:bg-orange-700 transition-colors font-medium flex items-center">
          <Plus size={16} className="mr-2" />
          Add Medication
        </button>
      </div>

      {/* Today's Schedule */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Today's Schedule</h2>
        <div className="space-y-4">
          {medications.map(med => (
            <div key={med.id} className="border border-gray-200 rounded-lg p-4">
              <div className="flex justify-between items-start mb-3">
                <div>
                  <h3 className="font-medium text-lg">{med.name}</h3>
                  <p className="text-sm text-gray-500">{med.type}</p>
                </div>
                <div className={`px-3 py-1 rounded-full text-sm font-medium ${
                  med.taken.every(t => t) ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
                }`}>
                  {med.taken.filter(t => t).length}/{med.taken.length} taken
                </div>
              </div>
              
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {med.times.map((time, i) => (
                  <div key={i} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                    <span className="font-medium">{time}</span>
                    <button
                      onClick={() => toggleMedication(med.id, i)}
                      className={`w-6 h-6 rounded-full flex items-center justify-center transition-colors ${
                        med.taken[i] 
                          ? 'bg-green-600 text-white' 
                          : 'bg-gray-200 text-gray-600 hover:bg-gray-300'
                      }`}
                    >
                      {med.taken[i] && <Check size={16} />}
                    </button>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Medication History */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Recent History</h2>
        <div className="space-y-3">
          {[
            { medication: 'Ibuprofen', time: 'Today, 8:00 AM', status: 'taken' },
            { medication: 'Vitamin D', time: 'Today, 9:00 AM', status: 'taken' },
            { medication: 'Ibuprofen', time: 'Yesterday, 8:00 PM', status: 'taken' },
            { medication: 'Ibuprofen', time: 'Yesterday, 2:00 PM', status: 'missed' },
          ].map((entry, i) => (
            <div key={i} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div>
                <p className="font-medium">{entry.medication}</p>
                <p className="text-sm text-gray-500">{entry.time}</p>
              </div>
              <div className={`px-3 py-1 rounded-full text-sm font-medium ${
                entry.status === 'taken' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
              }`}>
                {entry.status}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const Profile = () => {
  const [user, setUser] = useState(mockUser);
  const [notifications, setNotifications] = useState({
    pain_reminders: true,
    exercise_reminders: true,
    medication_reminders: true,
    educational_content: false,
  });

  return (
    <div className="space-y-6">
      <h1 className="text-2xl sm:text-3xl font-bold text-gray-800">Profile & Settings</h1>

      {/* User Info */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Personal Information</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Nickname</label>
            <input
              type="text"
              value={user.nickname}
              onChange={(e) => setUser({...user, nickname: e.target.value})}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
            <input
              type="email"
              value={user.email}
              onChange={(e) => setUser({...user, email: e.target.value})}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Birth Date</label>
            <input
              type="date"
              value={user.birth_date}
              onChange={(e) => setUser({...user, birth_date: e.target.value})}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Gender</label>
            <select
              value={user.gender}
              onChange={(e) => setUser({...user, gender: parseInt(e.target.value)})}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            >
              <option value={1}>Male</option>
              <option value={2}>Female</option>
              <option value={3}>Other</option>
            </select>
          </div>
        </div>
        <button className="mt-4 bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors font-medium">
          Save Changes
        </button>
      </div>

      {/* Notification Settings */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4 flex items-center">
          <Bell className="mr-2 text-blue-600" size={24} />
          Notification Preferences
        </h2>
        <div className="space-y-4">
          {Object.entries(notifications).map(([key, value]) => (
            <div key={key} className="flex items-center justify-between">
              <div>
                <p className="font-medium capitalize">
                  {key.replace(/_/g, ' ')}
                </p>
                <p className="text-sm text-gray-500">
                  {key === 'pain_reminders' && 'Daily reminders to log your pain levels'}
                  {key === 'exercise_reminders' && 'Reminders for your exercise schedule'}
                  {key === 'medication_reminders' && 'Alerts for medication times'}
                  {key === 'educational_content' && 'Weekly health tips and articles'}
                </p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={value}
                  onChange={(e) => setNotifications({...notifications, [key]: e.target.checked})}
                  className="sr-only peer"
                />
                <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>
          ))}
        </div>
      </div>

      {/* App Statistics */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4">Your Journey</h2>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">127</div>
            <p className="text-sm text-gray-600">Days Active</p>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-green-600">89</div>
            <p className="text-sm text-gray-600">Exercises Done</p>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-600">45</div>
            <p className="text-sm text-gray-600">Habits Formed</p>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-orange-600">98%</div>
            <p className="text-sm text-gray-600">Med Adherence</p>
          </div>
        </div>
      </div>

      {/* Account Actions */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold mb-4 text-red-600">Account Management</h2>
        <div className="space-y-3">
          <button className="w-full sm:w-auto bg-gray-600 text-white px-6 py-2 rounded-lg hover:bg-gray-700 transition-colors font-medium">
            Export My Data
          </button>
          <button className="w-full sm:w-auto bg-red-600 text-white px-6 py-2 rounded-lg hover:bg-red-700 transition-colors font-medium ml-0 sm:ml-3">
            Delete Account
          </button>
        </div>
        <p className="text-sm text-gray-500 mt-2">
          Account deletion is permanent and cannot be undone.
        </p>
      </div>
    </div>
  );
};

// Main App Component
const HealthWellnessApp = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isMobile, setIsMobile] = useState(false);
  const [showMobileMenu, setShowMobileMenu] = useState(false);

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768);
    };
    
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard': return <Dashboard />;
      case 'pain': return <PainTracker />;
      case 'exercises': return <Exercises />;
      case 'habits': return <Habits />;
      case 'content': return <Content />;
      case 'medications': return <Medications />;
      case 'profile': return <Profile />;
      default: return <Dashboard />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <div className="flex">
        {!isMobile && (
          <Navigation 
            activeTab={activeTab} 
            setActiveTab={setActiveTab}
            isMobile={isMobile}
            setShowMobileMenu={setShowMobileMenu}
          />
        )}
        
        <div className="flex-1">
          {isMobile && (
            <Navigation 
              activeTab={activeTab} 
              setActiveTab={setActiveTab}
              isMobile={isMobile}
              setShowMobileMenu={setShowMobileMenu}
            />
          )}
          
          <main className="p-4 sm:p-6 lg:p-8">
            {renderContent()}
          </main>
        </div>
      </div>

      <MobileMenu 
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        showMenu={showMobileMenu}
        setShowMenu={setShowMobileMenu}
      />
    </div>
  );
};

export default HealthWellnessApp;