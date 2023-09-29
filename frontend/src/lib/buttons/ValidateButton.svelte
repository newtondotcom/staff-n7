<script lang="ts">
    export let fct = () => {};
  </script>
    <button on:click={fct}>
      <slot></slot>
    </button>

<style lang="scss">
button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    margin: 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
}
</style>
  