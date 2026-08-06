<template>
    <div class="mx-3 mt-3">
        <h4>Ongoing Applied Applications</h4>
        <ApplicationTable :is-applied="true" :applications="appliedApplications" />
    </div>
</template>

<script>
import ApplicationTable from '../table-components/ApplicationTable.vue';

export default{
    components:{
        ApplicationTable
    },
    props: ["appliedApplications"]
}
</script>