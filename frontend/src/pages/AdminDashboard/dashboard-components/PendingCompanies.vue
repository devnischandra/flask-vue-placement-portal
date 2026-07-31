<template>
    <div class="mx-3 mt-3">
        <h4>Pending Companies</h4>
        <CompanyTable :companies="pendingCompanies"
        @update-company="(id, update) => $emit('update-company', id, update)"
        @update-user="(id, update) => $emit('update-user', id, update)"/>
    </div>
</template>

<script>
import CompanyTable from '../components/CompanyTable.vue';

export default {
    components:{
        CompanyTable
    },
    props: ["pendingCompanies"],
    emits:['update-company','update-user']
}
</script>