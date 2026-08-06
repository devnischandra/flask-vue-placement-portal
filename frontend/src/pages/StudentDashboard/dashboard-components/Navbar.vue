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
            <BaseButton @click="logout" type="button" btn-class="link" label="Logout" />
        </div>
    </nav>
</template>

<script>
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
    emits:['update-profile'],
    methods:{
        logout(){
            localStorage.removeItem("token")
            window.location.href = "/"
        }
    }
}
</script>