<script lang="ts">
    import ValidateButton from "$lib/buttons/ValidateButton.svelte";
</script>

<h1>Créer un évènement</h1>

<div class="container">
    <input type="datetime-local" id="birthdaytime" name="start">
    <input type="datetime-local" id="birthdaytime" name="end">
    <input type="text" id="eventname" name="eventname" placeholder="Nom">
    <input type="text" id="eventdescription" name="eventdescription" placeholder="Description / Consignes">
    <ValidateButton fct={() => console.log("test")}>Valider</ValidateButton>
</div>

<style lang="scss">
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

input {
    display: block;
}
</style>