<template>
    <component :is="currentView" />
</template>

<script>
import Login from './pages/Login.vue';
import RegisterCompany from './pages/RegisterCompany.vue';
import RegisterStudent from './pages/RegisterStudent.vue';
import AdminDashboard from './pages/AdminDashboard/AdminDashboard.vue';
import CompanyDashboard from './pages/CompanyDashboard/CompanyDashboard.vue';
import StudentDashboard from './pages/StudentDashboard/StudentDashboard.vue';

const routes = {
    '/': Login,
    '/register-company': RegisterCompany,
    '/register-student': RegisterStudent,
    '/admin-dashboard': AdminDashboard,
    '/company-dashboard': CompanyDashboard,
    '/student-dashboard': StudentDashboard
}

export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/']
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
		  this.currentPath = window.location.hash
		})
  }
}
</script>