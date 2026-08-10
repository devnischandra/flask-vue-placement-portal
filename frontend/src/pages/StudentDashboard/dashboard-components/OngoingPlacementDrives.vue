<template>
    <div class="mx-3 mt-3">
        <h4>Ongoing Placement Drives</h4>
            <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Company Name</th>
                    <th>Job Title</th>
                    <th>Started Date</th>
                    <th>End Date</th>
                    <th class="text-center">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="placement_drive in ongoingPlacementDrives" :key="placement_drive.id">
                    <td>{{ placement_drive.id }}</td>
                    <td>{{ placement_drive.company_name }}</td>
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
                        <h5>Company Details</h5>
                            <p>Company ID: {{placement_drive.company_id}}</p>
                            <p>Company Name: {{placement_drive.company_name}}</p>
                        <br/>
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
                        <BaseButton v-if="isEligible(placement_drive.minimum_cgpa) && !placement_drive.has_applied" class="ms-2" @click="$emit('create-application',placement_drive.id)" type="button" btn-class="outline-success" label="Apply" />
                        <BaseButton v-else-if="isEligible(placement_drive.minimum_cgpa) && placement_drive.has_applied" class="ms-2" type="button" btn-class="outline-secondary" label="Already applied" disabled/>
                        <BaseButton v-else class="ms-2" type="button" btn-class="outline-secondary" label="Not eligible" disabled/>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
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
    props: ["ongoingPlacementDrives", 'studentCgpa'],
    emits: ['create-application'],
    methods:{
        isEligible(min_cgpa) {
            return this.studentCgpa >= min_cgpa
        }
    }
}
</script>