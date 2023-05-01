<script>
	export let role;
</script>

{#if role != 'system'}
	<section class:user={role == 'user'}>
		<br />
		{#if role == 'user'}
			me:
		{:else}
			chatBot:
		{/if}
		<br />
		<slot />
	</section>
{/if}

<style>
	section {
		color: greenyellow;
		font-family: 'Courier New', monospace;
		font-size: small;
	}

	.user {
		color: white;
	}
</style>
