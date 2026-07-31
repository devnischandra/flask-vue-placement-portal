<template>
    <Navbar :current_user_name="current_user_name" @search="handleSearch" />
    <Stats v-if="!search.is_active" class="box-border" :stats="stats" />
    <PendingCompanies v-if="!search.is_active || pendingCompanies.length !== 0"
    class="box-border"
    :pending-companies="pendingCompanies"
    @update-company="updateCompany" 
    @update-user="updateUser" />
    <ApprovedCompanies v-if="!search.is_active || approvedCompanies.length !== 0"
    class="box-border" 
    :approved-companies="approvedCompanies"
    @update-user="updateUser" />
    <Students v-if="!search.is_active || searchStudents.length !== 0"
    class="box-border" 
    :students="searchStudents"
    @update-user="updateUser" />
    <PlacementDrives v-if="!search.is_active"
    class="box-border" 
    :placement_drives="placement_drives"
    @update-placement-drive="updatePlacementDrive" />
    <Applications v-if="!search.is_active"
    class="box-border" :applications="applications" />
</template>

<script>
import apiRequest from '@/apiRequest.js';
import Navbar from './dashboard-components/Navbar.vue';
import Search from './dashboard-components/Search.vue';
import Stats from './dashboard-components/Stats.vue';
import PendingCompanies from './dashboard-components/PendingCompanies.vue';
import ApprovedCompanies from './dashboard-components/ApprovedCompanies.vue';
import Students from './dashboard-components/Students.vue';
import PlacementDrives from './dashboard-components/PlacementDrives.vue';
import Applications from './dashboard-components/Applications.vue';

export default{
    components:{
        Navbar,
        Search,
        Stats,
        PendingCompanies,
        ApprovedCompanies,
        Students,
        PlacementDrives,
        Applications
    },
    data(){
        return{
            current_user_name:"",
            search:{
                is_active:false,
                search_by:"",
                value:""
            },
            stats:{
                "total_companies_count":0,
                "total_students_count":0,
                "total_placement_drives_count":0,
                "total_applications_count":0
            },
            companies:[],
            students:[],
            placement_drives:[],
            applications:[]
        }
    },
    created(){
        this.getMe(),
        this.getStats(),
        this.getCompanies(),
        this.getStudents(),
        this.getPlacementDrives(),
        this.getApplications()
    },
    computed:{
        pendingCompanies(){
            return this.searchCompanies.filter(c => c.status == "pending")
        },
        approvedCompanies(){
            return this.searchCompanies.filter( c => c.status == "approved")
        },
        searchCompanies(){
            if(!this.search.is_active) return this.companies
            let result = this.companies
            return this.search.search_by == "id" ? 
            result.filter(c => c.id == this.search.value):
            result.filter(c => c.name == this.search.value)
        },
        searchStudents(){
            if(!this.search.is_active) return this.students
            let result = this.students
            return this.search.search_by == "id" ? 
            result.filter(s => s.id == this.search.value):
            result.filter(s => s.name == this.search.value)
        }
    },
    methods:{
        async getMe(){
            const data = await apiRequest('/auth/me', 'GET')
            if (data.msg){
                return console.log(data.msg)
            }
            this.current_user_name = data.current_user_name
        },
        handleSearch(search){
            console.log("Search event:", search);
            this.search = {
                ...search
            }
        },
        async getStats(){
            const data = await apiRequest('/admin/stats', 'GET')
            this.stats = data
        },
        async getCompanies(){
            const data = await apiRequest('/admin/companies', 'GET')
            this.companies = data
        },
        async updateCompany(company_id, update){
            const data = await apiRequest(`/admin/companies/${company_id}`, 'PATCH', update)
            this.getCompanies()
            if (data.msg){
                console.log(data.msg)
            }
        },
        async getStudents(){
            const data = await apiRequest('/admin/students', 'GET')
            this.students = data
        },
        async updateUser(user_id, update){
            const data = await apiRequest(`/admin/users/${user_id}`, 'PATCH', update)
            this.getCompanies()
            this.getStudents()
            if (data.msg){
                console.log(data.msg)
            }
        },
        async getPlacementDrives(){
            const data = await apiRequest('/admin/placement-drives', 'GET')
            this.placement_drives = data
        },
        async updatePlacementDrive(placement_drive_id, update){
            const data = await apiRequest(`/admin/placement-drives/${placement_drive_id}`, 'PATCH', update)
            this.getPlacementDrives()
            if (data.msg){
                console.log(data.msg)
            }
        },
        async getApplications(){
            const data = await apiRequest('/admin/applications', 'GET')
            this.applications = data
        },
        async getStudent(student_id){
            const data = await apiRequest(`/admin/students/${student_id}`, 'GET')
            if (data.msg){
                return console.log(data.msg)
            }
            this.student = data
        },

    }
}

</script>