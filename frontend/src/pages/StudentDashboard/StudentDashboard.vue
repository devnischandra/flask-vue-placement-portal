<template>
    <Navbar :applications="applications" :current-user="currentUser" @update-profile="updateProfile" />
    <Companies class="box-border" :companies="companies" />
    <OngoingPlacementDrives class="box-border" :student-cgpa="currentUser.cgpa" :ongoing-placement-drives="ongoingPlacementDrives"
    @create-application="createApplication" />
    <AppliedApplications class="box-border" :applied-applications="appliedApplications" />
</template>

<script>
import apiRequest from '@/apiRequest.js';
import Navbar from './dashboard-components/Navbar.vue';
import OngoingPlacementDrives from './dashboard-components/OngoingPlacementDrives.vue';
import AppliedApplications from './dashboard-components/AppliedApplications.vue';
import Companies from './dashboard-components/Companies.vue';

export default{
    components:{
        Navbar,
        Companies,
        OngoingPlacementDrives,
        AppliedApplications
    },
    data(){
        return{
            currentUser:"",
            companies:"",
            placement_drives: [],
            applications:[]
        }
    },
    created(){
        this.getMe(),
        this.getCompanies(),
        this.getPlacementDrives(),
        this.getApplications()
    },
    computed:{
        ongoingPlacementDrives(){
            return this.placement_drives.filter(placement_drive => this.isActive(placement_drive))
        },
        appliedApplications() {
            return this.applications.filter(application =>
            this.ongoingPlacementDrives.some(
            drive => drive.id === application.placement_drive_id
        )
    )
}
    },
    methods:{
        async getMe(){
            const data = await apiRequest('/student/', 'GET')
            this.currentUser = {...data}
        },
        async updateProfile(update){
            const data = await apiRequest('/student/', 'POST', update)
            this.getMe()
            if (data.msg){
                console.log(data.msg)
            }
        },
        async getCompanies(){
            const data = await apiRequest('/student/companies','GET')
            this.companies = data
        },
        async getPlacementDrives(){
            const data = await apiRequest('/student/placement-drives','GET')
            this.placement_drives = data
        },
        isActive(placement_drive){
            const today = new Date()
            const start = new Date(placement_drive.start_date)
            const end = new Date(placement_drive.end_date)

            return today >= start && today <= end
        },
        async getApplications(){
            const data = await apiRequest('/student/applications','GET')
            this.applications = data
        },
        async createApplication(placement_drive_id){
            const data = await apiRequest('/student/applications','POST', {placement_drive_id})
            await this.getPlacementDrives()
            await this.getApplications()
            if(data.msg){
                console.log(data.msg)
            }
        }
    }
}
</script>