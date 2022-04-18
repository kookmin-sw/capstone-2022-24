<template>
	<div class="row q-mt-md filter-frame">
		<div class="col-2 q-mt-auto q-mb-auto">{{ this.filterName }}</div>
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
// import { mapActions } from 'vuex';

export default {
	name: 'Filter',
	props: {
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
		};
	},
	methods: {
		clickCondition(cond) {
			// console.log(cond.label, cond.isSelect);
			// 선택
			if (cond.isSelect) {
				if (cond.label === '전체') {
					this.conditions.forEach(cond => {
						this.selected.add(cond.label);
					});
					// console.log(this.selected);
					return;
				}
				this.selected.add(cond.label);
				// console.log(this.selected);
			}
			// 선택 취소
			else {
				if (cond.label === '전체') {
					this.conditions.forEach(cond => {
						if (!cond.isSelect) {
							this.selected.delete(cond.label);
						}
					});
					// console.log(this.selected);
					return;
				}
				this.selected.delete(cond.label);
				// console.log(this.selected);
			}
		},
	},
};
</script>

<style scoped></style>
