<template>
	<div class="row q-mt-md filter-frame">
		<div class="col-2 q-mt-auto q-mb-auto">{{ this.filterLabel }}</div>
		<q-separator vertical inset color="blue" />
		<div class="col-9 q-ml-sm text-left chips-frame">
			<q-chip
				outline
				color="blue"
				v-for="condition in conditions"
				:key="condition.key"
				v-model:selected="condition.isSelect"
				@click="clickCondition(condition)">
				{{ condition.label }}
			</q-chip>
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
		clickCondition(cond) {
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
			this.$store.dispatch('videoList/selectCondition', condition);
		},
	},
};
</script>

<style scoped></style>
