<script>
import { fetchEvents } from '@/api/events';
import Navbar from '../Navbar.vue';
import CustomFooter from '../CustomFooter.vue';

export default {
	components: {
		Navbar,
		CustomFooter,
},
	data() {
		return {
			events: [],
			currentPage: 1,
			perPage: 20
		}
	},
	computed: {
		filteredEvents() {
			return this.events.slice(1);
		},
		limitedEvents() {
			const start = (this.currentPage - 1) * this.perPage;
			return this.filteredEvents.slice(start, start + this.perPage);
		},
		totalPages() {
			return Math.ceil(this.filteredEvents.length / this.perPage);
		},
		pageNumbers() {
			const pages = [];
			for (let i = 1; i <= this.totalPages; i++) {
				pages.push(i);
			}
			return pages;
		}
	},
	methods: {
		nextPage() {
			if (this.currentPage < this.totalPages) {
				this.currentPage++;
			}
		},
		prevPage() {
			if (this.currentPage > 1) {
				this.currentPage--;
			}
		},
		setPage(pageNumber) {
			if (pageNumber >= 1 && pageNumber <= this.totalPages) {
				this.currentPage = pageNumber;
			}
		}
	},
	created() {
		fetchEvents()
			.then(data => {
				this.events = data;
			})
			.catch(error => {
				console.error('There was a problem fetching the events:', error);
			});
	}
}
</script>
<template>
	<div class="page-container">
		<navbar />
		<div class="container mt-4">
			<div class="d-flex justify-content-center align-items-center">
				<div class="card shadow">
					<div class="card-body">
						<h1 class="card-title">Events</h1>
						<div class="table-responsive">
							<table class="table">
								<thead class="thead-light">
									<tr>
										<th>Event/Programme</th>
										<th>Date</th>
										<th>Venue</th>
									</tr>
								</thead>
								<tbody>
									<tr v-for="event in limitedEvents" :key="event.id">
										<td>{{ event.name }}</td>
										<td>{{ event.date }}</td>
										<td>{{ event.venue }}</td>
									</tr>
								</tbody>
							</table>
						</div>
						<nav v-if="totalPages > 1">
							<ul class="pagination">
								<li class="page-item" :class="{ disabled: currentPage === 1 }">
									<a class="page-link" href="#" @click.prevent="setPage(1)">First</a>
								</li>
								<li class="page-item" :class="{ disabled: currentPage === 1 }">
									<a class="page-link" href="#" aria-label="Previous" @click.prevent="prevPage">
										<span aria-hidden="true">&laquo;</span>
									</a>
								</li>
								<li class="page-item" v-for="page in pageNumbers" :class="{ active: currentPage === page }" :key="page">
									<a class="page-link" href="#" @click.prevent="setPage(page)">{{ page }}</a>
								</li>
								<li class="page-item" :class="{ disabled: currentPage === totalPages }">
									<a class="page-link" href="#" aria-label="Next" @click.prevent="nextPage">
										<span aria-hidden="true">&raquo;</span>
									</a>
								</li>
								<li class="page-item" :class="{ disabled: currentPage === totalPages }">
									<a class="page-link" href="#" @click.prevent="setPage(totalPages)">Last</a>
								</li>
							</ul>
						</nav>
						<p v-if="limitedEvents.length === 0">No events found.</p>
					</div>
				</div>
			</div>
		</div>
		<custom-footer />
	</div>
</template>

<style scoped>
.page-container {
	display: flex;
	flex-direction: column;
	min-height: 100vh;
}

.container {
	flex: 1;
	padding-top: 1rem;
}

.table-responsive {
	overflow-x: auto;
}

.custom-footer {
	margin-top: auto;
}

@media (max-width: 768px) {
	.table {
		font-size: smaller;
	}
}
</style>