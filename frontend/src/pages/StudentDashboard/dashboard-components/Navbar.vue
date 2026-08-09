<template>
    <nav class="navbar bg-body-tertiary p-3">
        <div class="container-fluid">
            <a class="navbar-brand">hi, {{ currentUser.name }}</a>
            <BaseModalTriggerButton id="student-application" trigger-btn-label="History" />
            <BaseModal id="student-application" modal-title="Student Application History">
                <ApplicationTable :applications="applications" />
            </BaseModal>
            <BaseModalTriggerButton id="update-profile" trigger-btn-label="Update Profile" />
            <BaseModal id="update-profile" modal-title="Update Profile">
                <UpdateProfile  v-if="currentUser" :current-user="currentUser" @update-profile="$emit('update-profile',$event)" />
            </BaseModal>
            <BaseButton
                @click="processExport"
                type="button"
                btn-class="primary"
                :label="is_exporting ? 'Processing...' : (filename ? 'Download CSV' : 'Export CSV')"
                :disabled="is_exporting"
            />
            <BaseButton @click="logout" type="button" btn-class="link" label="Logout" />
        </div>
    </nav>
</template>

<script>
import apiRequest from '@/apiRequest';
import BaseModalTriggerButton from '@/components/BaseModalTriggerButton.vue';
import BaseModal from '@/components/BaseModal.vue';
import BaseButton from '@/components/BaseButton.vue';
import UpdateProfile from './UpdateProfile.vue';
import ApplicationTable from '../table-components/ApplicationTable.vue';


export default{
    components:{
        BaseModalTriggerButton,
        BaseModal,
        ApplicationTable,
        BaseButton,
        UpdateProfile
    },
    props: ["currentUser", "applications"],
    data(){
        return {
            is_exporting:false,
            task_id:"",
            filename:""
        }
    },
    emits:['update-profile'],
    methods:{
        logout(){
            localStorage.removeItem("token")
            window.location.href = "/"
        },
        async processExport(){
            if (!this.filename){
                this.is_exporting = true
                const data = await apiRequest('/student/export-applications', 'POST')
                if (data.msg){
                    console.log(data.msg)
                }
                this.task_id = data.id
                this.checkExportStatus()
            }
            else{
                window.location.href = `http://127.0.0.1:5000/${this.filename}`
            }
        },
        async checkExportStatus(){
            const data = await apiRequest(`/common/celery-task-status/${this.task_id}`,'GET')
            const status = data.status
            
            if (status=='COMPLETED'){
                this.is_exporting = false
                alert('CSV export COMPLETED!')
                this.filename = data.filename
                return
            }

            if (status=='FAILED'){
                this.is_exporting = false
                alert('CSV export FAILED!')
                return
            }

            setTimeout(() => {
                this.checkExportStatus()
            }, 2000);
        }
    }
}
</script>