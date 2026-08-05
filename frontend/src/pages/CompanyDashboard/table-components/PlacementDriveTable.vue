<template>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Job Title</th>
                <th>Start Date</th>
                <th>End Date</th>
                <th class="text-center">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="placement_drive in placementDrives" :key="placement_drive.id">
                <td>{{ placement_drive.id }}</td>
                <td>{{ placement_drive.job_title }}</td>
                <td>{{ placement_drive.start_date }}</td>
                <td>{{ placement_drive.end_date }}</td>
                <td class="text-center">
                    <!-- modal-trigger-btn -->
                    <BaseModalTriggerButton
                    :id="`placement_drive-${placement_drive.id}`"
                    trigger-btn-label="View" />
                    <!-- modal-body -->
                    <BaseModal
                    :id="`placement_drive-${placement_drive.id}`"
                    :modal-title="`Placement Drive #${placement_drive.id}`"
                    >
                    <h5>Job Details</h5>
                        <p>Title: {{placement_drive.job_title}}</p>
                        <p>Mode: {{placement_drive.job_mode}}</p>
                        <p>Location: {{placement_drive.location || "Not Provided"}}</p>
                    <br/>
                    <h5>Job Description</h5>
                        <p>{{ placement_drive.description }}</p>
                    <br/>
                    <h5>Eligibility Criteria</h5>
                        <p>Minimum CGPA: {{ placement_drive.minimum_cgpa }}</p>
                    <br/>
                    <h5>Important Dates</h5>
                        <p>Start Date: {{ placement_drive.start_date }}</p>
                        <p>End Date: {{ placement_drive.end_date }}</p>
                    </BaseModal>
                    <BaseButton v-if="isActive(placement_drive)" class="ms-2" @click="$emit('update-placement-drive',placement_drive.id, {'end_date':true})" type="button" btn-class="outline-success" label="Mark As Complete" />
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import BaseModalTriggerButton from '@/components/BaseModalTriggerButton.vue';
import BaseModal from '@/components/BaseModal.vue';
import BaseButton from '@/components/BaseButton.vue';

export default{
    components:{
        BaseModalTriggerButton,
        BaseModal,
        BaseButton
    },
    props: ["placementDrives"],
    emits: ['update-placement-drive'],
    methods:{
        isActive(placement_drive) {
            const today = new Date();
            const start = new Date(placement_drive.start_date);
            const end = new Date(placement_drive.end_date);

            return today >= start && today <= end;
        }
    }
}
</script>