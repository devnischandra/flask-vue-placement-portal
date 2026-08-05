<template>
    <div class="mx-3 mt-3">
        <h4>Applied Candidates</h4>
        <ApplicationTable @update-application-status="(id, update) => $emit('update-application-status',id, update)" :applications="appliedCandidates" />
    </div>
</template>

<script>
import ApplicationTable from '../table-components/ApplicationTable.vue';

export default {
    components:{
        ApplicationTable
    },
    props: ["appliedCandidates"],
    emits:['update-application-status']
}
</script>