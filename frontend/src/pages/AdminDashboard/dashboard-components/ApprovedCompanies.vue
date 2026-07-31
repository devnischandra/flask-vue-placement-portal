<template>
    <div class="mx-3 mt-3">
        <h4>Approved Companies</h4>
        <CompanyTable :companies="approvedCompanies"
        @update-user="(id, update) => $emit('update-user', id, update)"/>
    </div>
</template>

<script>
import CompanyTable from '../components/CompanyTable.vue';

export default {
    components:{
        CompanyTable
    },
    props: ["approvedCompanies"],
    emits:['update-user']
}
</script>