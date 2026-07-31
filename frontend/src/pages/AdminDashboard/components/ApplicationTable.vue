<template>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Student ID</th>
                <th>Placement Drive ID</th>
                <th>Applied Date</th>
                <th>Status</th>
                <th class="text-center">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="application in applications" :key="application.id">
                <td>{{ application.id }}</td>
                <td>{{ application.student_id }}</td>
                <td>{{ application.placement_drive_id }}</td>
                <td>{{ application.applied_date }}</td>
                <td>{{ application.status }}</td>
                <td class="text-center">
                    <BaseModalTriggerButton
                    @open-modal="() => getStudent(application.student_id)"
                    :id="`application-${application.id}`"
                    trigger-btn-label="View" />
                    <BaseModal
                    :id="`application-${application.id}`"
                    :modal-title="`Student Application #${application.id}`"
                    :is-modal-btn-label="false" >
                    <h5>Application Details</h5>
                        <p>Application ID: {{application.id}}</p>
                        <p>Applied Date: {{application.applied_date}}</p>
                        <p>Status: {{ application.status }}</p>
                        <p>Interview Date: {{ application.interview_date || "Not Scheduled" }}</p>
                        <p>Company Feedback: {{ application.company_feedback || "NA" }}</p>
                    <br/>
                    <h5>Student Details</h5>
                        <p>Id: {{ student?.id }}</p>
                        <p>Name: {{ student?.name }}</p>
                        <p>Email: {{ student?.email }}</p>
                        <p>Gender: {{ student?.gender  }}</p>
                        <p>Date of Birth: {{ student?.date_of_birth  }}</p>
                    <br />
                    <h5>Education Details</h5>
                        <p>Department: {{ student?.department  }}</p>
                        <p>CGPA: {{ student?.cgpa  }}</p>
                        <p>Resume URL: 
                            <a  v-if="student?.resume_url" :href="student?.resume_url"> View Resume </a>
                            <p v-else>Not Available</p>
                        </p>
                    </BaseModal>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import BaseModalTriggerButton from '@/components/BaseModalTriggerButton.vue';
import BaseModal from '@/components/BaseModal.vue';
import apiRequest from '@/apiRequest';


export default{
    components:{
        BaseModalTriggerButton,
        BaseModal
    },
    props: ["applications"],
    data(){
        return{
            student:{}
        }
    },
    methods:{
        async getStudent(student_id){
            this.student = await apiRequest(`/admin/students/${student_id}`,'GET')
        }
    }
}
</script>