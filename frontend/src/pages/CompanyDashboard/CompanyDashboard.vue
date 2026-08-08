<template>
    <Navbar :current_user_name="current_user_name" />
    <OngoingPlacementDrives class="box-border" @update-placement-drive="updatePlacementDrive" :ongoing-placement-drives="ongoingPlacementDrives" @create-placement-drive="createPlacementDrive" />
    <ClosedPlacementDrives class="box-border" :closed-placement-drives="closedPlacementDrives" />
    <AppliedCandidates class="box-border" @update-application-status="updateApplicationStatus" :applied-candidates="appliedCandidates"/>
    <ShortlistedCandidates class="box-border" @update-application-status="updateApplicationStatus" :shortlisted-candidates="shortlistedCandidates" />
    <InterviewCandidates class="box-border" @update-application-status="updateApplicationStatus" :interview-candidates="interviewCandidates" />
    <SelectedCandidates class="box-border" :selected-candidates="selectedCandidates" />
</template>

<script>
import apiRequest from '@/apiRequest.js';
import Navbar from './dashboard-components/Navbar.vue';
import OngoingPlacementDrives from './dashboard-components/OngoingPlacementDrives.vue';
import ClosedPlacementDrives from './dashboard-components/ClosedPlacementDrives.vue';
import AppliedCandidates from './dashboard-components/AppliedCandidates.vue';
import ShortlistedCandidates from './dashboard-components/ShortlistedCandidates.vue';
import InterviewCandidates from './dashboard-components/InterviewCandidates.vue';
import SelectedCandidates from './dashboard-components/SelectedCandidates.vue';

export default{
    components:{
        Navbar,
        OngoingPlacementDrives,
        ClosedPlacementDrives,
        AppliedCandidates,
        ShortlistedCandidates,
        InterviewCandidates,
        SelectedCandidates
    },
    data(){
        return{
            current_user_name:"",
            placement_drives: [],
            applications:[]
        }
    },
    created(){
        this.getMe(),
        this.getPlacementDrives(),
        this.getApplications()
    },
    computed:{
        ongoingPlacementDrives(){
            return this.placement_drives.filter(placement_drive => this.isActive(placement_drive))
        },
        closedPlacementDrives(){
            return this.placement_drives.filter(placement_drive => !this.isActive(placement_drive))
        },
        appliedCandidates() {
            return this.applications.filter(application =>
                application.status === "applied" &&
                this.ongoingPlacementDrives.some(
                    drive => drive.id === application.placement_drive_id
                )
            )
        },
        shortlistedCandidates() {
            return this.applications.filter(application =>
                application.status === "shortlisted" &&
                !application.interview_date &&
                this.ongoingPlacementDrives.some(
                    drive => drive.id === application.placement_drive_id
                )
            )
        },
        interviewCandidates() {
            return this.applications.filter(application =>
                application.status === "shortlisted" &&
                application.interview_date &&
                this.ongoingPlacementDrives.some(
                    drive => drive.id === application.placement_drive_id
                )
            )
        },
        selectedCandidates() {
            return this.applications.filter(application =>
               application.status === "selected" &&
                this.ongoingPlacementDrives.some(
                    drive => drive.id === application.placement_drive_id
                )
            )
        }
    },
    methods:{
        async getMe(){
            const data = await apiRequest('/auth/me', 'GET')
            this.current_user_name = data.current_user_name
        },
        async createPlacementDrive(new_placement_drive){
            const data = await apiRequest('/company/placement-drives','POST', new_placement_drive)
            this.getPlacementDrives()
        },
        async getPlacementDrives(){
            const data = await apiRequest('/company/placement-drives','GET')
            this.placement_drives = data.filter(pd => !pd.is_blacklisted)
        },
        async getPlacementDrive(placement_drive_id){
            const placement_drive = await apiRequest(`/company/placement-drives/${placement_drive_id}`,'GET')
            return placement_drive
        },
        isActive(placement_drive){
            const today = new Date()
            const start = new Date(placement_drive.start_date)
            const end = new Date(placement_drive.end_date)

            return today >= start && today <= end
        },
        async updatePlacementDrive(placement_drive_id, update){
            const data = await apiRequest(`/company/placement-drives/${placement_drive_id}`, 'PATCH', update)
            this.getPlacementDrives()
            if (data.msg){
                return console.log(data.msg)
            }
        },
        async getApplications(){
            const data = await apiRequest('/company/applications','GET')
            this.applications = data
        },
        async updateApplicationStatus(application_id, update){
            const data = await apiRequest(`/company/applications/${application_id}`, 'PATCH', update)
            this.getApplications()
            if (data.msg){
                return console.log(data.msg)
            }
        }
    }
}
</script>