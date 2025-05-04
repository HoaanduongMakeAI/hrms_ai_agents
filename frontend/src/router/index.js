import { createRouter, createWebHistory } from 'vue-router';

// Import views here (we will add them later)
import ApplicationFormView from '../views/ApplicationFormView.vue';
import DepartmentDetailsView from '../views/DepartmentDetailsView.vue';
import DepartmentListView from '../views/DepartmentListView.vue';
import EmployeeListView from '../views/EmployeeListView.vue';
import EmployeeProfileView from '../views/EmployeeProfileView.vue';
import InterviewFormView from '../views/InterviewFormView.vue';
import InterviewListView from '../views/InterviewListView.vue';
import JobOpeningFormView from '../views/JobOpeningFormView.vue';
import JobOpeningListView from '../views/JobOpeningListView.vue';
import PerformanceFormView from '../views/PerformanceFormView.vue';
import PerformanceListView from '../views/PerformanceListView.vue';
import PositionDetailsView from '../views/PositionDetailsView.vue';
import PositionListView from '../views/PositionListView.vue';
import ResignationFormView from '../views/ResignationFormView.vue';
import ResignationListView from '../views/ResignationListView.vue';
import ConversationView from '../views/ConversationView.vue';
import MainView from '../views/MainView.vue';


const routes = [
  // Define routes here
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/conversation',
    name: 'conversation',
    component: ConversationView
  },
  {
    path: '/application-form',
    name: 'application-form',
    component: ApplicationFormView
  },
  {
    path: '/department-details',
    name: 'department-details',
    component: DepartmentDetailsView
  },
  {
    path: '/department-list',
    name: 'department-list',
    component: DepartmentListView
  },
  {
    path: '/employee-list',
    name: 'employee-list',
    component: EmployeeListView
  },
  {
    path: '/employee-profile',
    name: 'employee-profile',
    component: EmployeeProfileView
  },
  {
    path: '/interview-form',
    name: 'interview-form',
    component: InterviewFormView
  },
  {
    path: '/interview-list',
    name: 'interview-list',
    component: InterviewListView
  },
  {
    path: '/job-opening-form',
    name: 'job-opening-form',
    component: JobOpeningFormView
  },
  {
    path: '/job-opening-list',
    name: 'job-opening-list',
    component: JobOpeningListView
  },
  {
    path: '/performance-form',
    name: 'performance-form',
    component: PerformanceFormView
  },
  {
    path: '/performance-list',
    name: 'performance-list',
    component: PerformanceListView
  },
  {
    path: '/position-details',
    name: 'position-details',
    component: PositionDetailsView
  },
  {
    path: '/position-list',
    name: 'position-list',
    component: PositionListView
  },
  {
    path: '/resignation-form',
    name: 'resignation-form',
    component: ResignationFormView
  },
  {
    path: '/resignation-list',
    name: 'resignation-list',
    component: ResignationListView
  },
];

const router = createRouter({
  history: createWebHistory('/hrms_ai_agents'), // Set base path for Frappe access
  routes
});

export default router;