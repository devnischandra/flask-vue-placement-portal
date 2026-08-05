<template>
    <div class="mx-3 mt-3">
        <h4>Interview Details</h4>
        <ApplicationTable @update-application-status="(id, update) => $emit('update-application-status',id, update)" :applications="interviewCandidates" />
    </div>
</template>

<script>
import ApplicationTable from '../table-components/ApplicationTable.vue';

export default {
    components:{
        ApplicationTable
    },
    props: ["interviewCandidates"],
    emits:['update-application-status']
}
</script>