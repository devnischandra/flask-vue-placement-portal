<template>
    <div class="mx-3 mt-3">
        <h4>Companies</h4>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Company Name</th>
                    <th>Email</th>
                    <th>HR Contact</th>
                    <th>Website URL</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="company in companies" :key="company.id">
                    <td>{{ company.id }}</td>
                    <td>{{ company.name }}</td>
                    <td>{{ company.email }}</td>
                    <td>{{ company.hr_contact || 'NA' }}</td>
                    <td>
                        <a v-if="company.website_url" :href="company.website_url">website link</a>
                        <p v-else>Link Not Provided</p>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default{
    props: ["companies"]
}
</script>