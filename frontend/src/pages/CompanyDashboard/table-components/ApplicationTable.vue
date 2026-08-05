<template>
    <table class="table">
        <thead>
            <tr>
                <th>Application ID</th>
                <th>Drive ID</th>
                <th>Student ID</th>
                <th>Applied Date</th>
                <th class="text-center">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="application in applications" :key="application.id">
                <td>{{ application.id }}</td>
                <td>{{ application.placement_drive_id }}</td>
                <td>{{ application.student_id }}</td>
                <td>{{ application.applied_date }}</td>
                <td class="text-center">
                    <!-- modal-trigger-btn -->
                    <BaseModalTriggerButton
                    @open-modal="getStudent(application.student_id)"
                    :id="`application-${application.id}`"
                    trigger-btn-label="View" />
                    <!-- modal-body -->
                    <BaseModal
                    :id="`application-${application.id}`"
                    :modal-title="`Student Application #${application.id}`"
                    >
                    <h5>Student Details</h5>
                        <p>ID: {{student?.id}}</p>
                        <p>Name: {{student?.name}}</p>
                        <p>Email: {{student?.email}}</p>
                        <p>Gender: {{student?.gender}}</p>
                        <p>Date of Birth: {{student?.date_of_birth}}</p>
                    <br/>
                    <h5>Education Details</h5>
                        <p>Department: {{ student?.department }}</p>
                        <p>CGPA: {{ student?.cgpa }}</p>
                        <p>Resume URL: {{ student?.resume_url }}</p>
                    <br/>
                    <h5>Current Status</h5>
                        <p>Current Status: {{ application.status }}</p>
                        <p>Current Status: {{ application.company_feedback || "NA" }}</p>
                    <br />
                    </BaseModal>
                    <div v-if="application.status == 'applied'" class="d-inline">
                        <BaseButton class="ms-2"
                        @click="$emit('update-application-status', application.id, {'status':'shortlisted'})"
                        type="button" btn-class="outline-success" label="Shortlist Candidate" />
                        <BaseButton class="ms-2"
                        @click="$emit('update-application-status', application.id, {'status':'rejected'})" 
                        type="button" btn-class="outline-danger" label="Reject Candidate" />
                    </div>
                    <div v-if="application.status == 'shortlisted' && !application.interview_date" class="box-border text-start mt-2">
                        <form @submit.prevent="$emit('update-application-status', application.id,  {'interview_date': interviewDates[application.id]})">
                            <BaseInput :id="`interview_date_${application.id}`" type="date" label="Schedule Interview"  v-model="interviewDates[application.id]" />
                            <BaseButton type="submit" btn-class="primary" label="Submit" />
                        </form>
                    </div>
                    <div v-if="application.status == 'shortlisted' && application.interview_date" class="d-inline">
                        <BaseButton class="ms-2"
                        @click="$emit('update-application-status', application.id, {'status':'selected'})"
                        type="button" btn-class="outline-success" label="Select Candidate" />
                        <BaseButton class="ms-2"
                        @click="$emit('update-application-status', application.id, {'status':'rejected'})" 
                        type="button" btn-class="outline-danger" label="Reject Candidate" />
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import apiRequest from '@/apiRequest';
import BaseModalTriggerButton from '@/components/BaseModalTriggerButton.vue';
import BaseModal from '@/components/BaseModal.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseInput from '@/components/BaseInput.vue';

export default{
    components:{
        BaseModalTriggerButton,
        BaseModal,
        BaseButton,
        BaseInput
    },
    props: ["applications"],
    emits: ['update-application-status'],
    data(){
        return{
            updateApplication:{
                status: "",
                company_feedback:"",
            },
            student:{},
            interviewDates: {}
        }
    },
    methods:{
        async getStudent(student_id){
            const data = await apiRequest(`/company/students/${student_id}`,'GET')
            this.student = data
        },
    }
}
</script>