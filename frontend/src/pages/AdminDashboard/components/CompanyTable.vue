<template>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>HR Contact</th>
                <th>Website Url</th>
                <th class="text-center">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="company in companies" :key="company.id">
                <td>{{ company.id }}</td>
                <td>{{ company.name }}</td>
                <td>{{ company.email }}</td>
                <td>{{ company.hr_contact || 'Not Provided' }}</td>
                <td>{{ company.website_url || 'Not Provided' }}</td>
                <td class="text-center">
                    <a  v-if="company.website_url" :href="company.website_url"> Visit Website </a>
                    <p v-else>Not Available</p>
                </td>
                <td v-if="company.status == 'pending'" class="text-center">
                    <BaseButton class="me-3" @click="$emit('update-company',company.id, {'status':'approved'})" type="button" btn-class="outline-success" label="Approve" />
                    <BaseButton @click="$emit('update-company',company.id, {'status':'rejected'})" type="button" btn-class="outline-danger" label="Reject" />
                </td>
                <td v-if="company.status == 'approved'" class="text-center">
                    <BaseButton @click="$emit('update-user',company.id, {'is_blacklisted': true})" type="button" btn-class="primary" :label="company.is_blacklisted ? 'Unblock': 'Block' " />
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';

export default{
    components:{
        BaseButton
    },
    props: ["companies"],
    emits:['update-company','update-user']
}
</script>