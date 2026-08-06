<template>
    <table class="table">
        <thead>
            <tr>
                <th>Application ID</th>
                <th v-if="!isApplied">Is Active</th>
                <th>Drive ID</th>
                <th>Company Name</th>
                <th>Job Title</th>
                <th>Applied Date</th>
                <th>Status</th>
                <th>Interview Date</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="application in applications" :key="application.id">
                <td>{{ application.id }}</td>
                <td v-if="!isApplied">{{ isActive(application.placement_drive_start_date, application.placement_drive_end_date) ? "Active" : "Not Active" }}</td>
                <td>{{ application.placement_drive_id }}</td>
                <td>{{ application.company_name }}</td>
                <td>{{ application.job_title }}</td>
                <td>{{ application.applied_date }}</td>
                <td>{{ application.status }}</td>
                <td>{{ application.interview_date || "NA" }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default{
    props: ["applications", "isApplied"],
    methods:{
        isActive(start, end){
            const today = new Date()
            const start_date = new Date(start)
            const end_date = new Date(end)

            return today >= start_date && today <= end_date
        }
    }
}
</script>