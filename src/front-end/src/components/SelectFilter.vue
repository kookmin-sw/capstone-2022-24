<template>
	<div class="row q-mt-md">
		<div class="col-2 q-mt-auto q-mb-auto">{{ this.filterLabel }}</div>
		<q-separator vertical inset color="blue-4" />
		<div class="col-9 q-ml-sm text-left">
			<span v-for="condition in conditions" :key="condition.key">
				<!--  select -->
				<q-chip
					v-if="condition.isSelect"
					v-model:selected="condition.isSelect"
					class="bg-blue-80 text-weight-bold text-grey-100"
					@click="clickCondition(condition)">
					{{ condition.label }}
				</q-chip>
				<!-- not select -->
				<q-chip
					v-else
					outline
					class="radius-50 border-blue-200 text-grey-100"
					id="chip"
					v-model:selected="condition.isSelect"
					@click="clickCondition(condition)">
					{{ condition.label }}
				</q-chip>
			</span>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Filter',
	props: {
		filterLabel: {
			type: String,
			require: true,
		},
		filterName: {
			type: String,
			require: true,
		},
		conditions: {
			require: true,
		},
	},
	data() {
		return {
			selected: new Set(),
			isAllSelect: false,
		};
	},
	methods: {
		async clickCondition(cond) {
			// 선택
			if (cond.isSelect) {
				if (cond.label === '전체') {
					this.conditions.forEach(cond => {
						this.selected.add(cond.name);
					});
					this.selected.delete('all');
					this.isAllSelect = true;
				} else {
					this.selected.add(cond.name);
				}
			}
			// 선택 취소
			else {
				if (cond.label === '전체') {
					this.conditions.forEach(cond => {
						if (!cond.isSelect) {
							this.selected.delete(cond.name);
						}
					});
					this.isAllSelect = false;
				} else if (!this.isAllSelect) {
					this.selected.delete(cond.name);
				}
			}
			const condition = {
				name: this.filterName,
				selected: this.selected,
			};
			await this.$store.dispatch('videoList/filterVideos', condition);
		},
	},
};
</script>

<style scoped></style>
