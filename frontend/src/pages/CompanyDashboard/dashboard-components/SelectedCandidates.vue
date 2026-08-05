<template>
    <div class="mx-3 mt-3">
        <h4>Selected Candidates</h4>
        <ApplicationTable :applications="selectedCandidates" />
    </div>
</template>

<script>
import ApplicationTable from '../table-components/ApplicationTable.vue';

export default {
    components:{
        ApplicationTable
    },
    props: ["selectedCandidates"]
}
</script>