from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey, desc
from sqlalchemy.orm import relationship
from .base import Base
import csv
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class GovernmentRequestsReport(Base):
	__tablename__ = 'government_requests_reports'
	report_id=Column(Integer, primary_key=True)
	transparency_report_id=Column(Integer, ForeignKey('transparency_reports.report_id'))
	inclusion_status=Column(Boolean)
	complete_status=Column(Boolean)
	date_updated=Column(Date)
	narrative=Column(Text)
	transparency_report=relationship('TransparencyReport', back_populates="government_requests_report")
	disclosures=relationship('GovernmentRequestReportTypeDisclosure', back_populates="report", cascade="delete, save-update")

	def serialize(self):
		return {
			'report_id': self.report_id,
			'transparency_report_id': self.transparency_report_id,
			'inclusion_status': self.inclusion_status,
			'complete_status': self.complete_status,
			'narrative': self.narrative,
			'categorized_disclosures': self.serializeDisclosures(),
			'date_updated': self.date_updated.strftime('%Y-%m-%d') if self.date_updated else None
		}
	def serializeDisclosures(self):
		categories = {}
		for disclosure in self.disclosures:
			category = disclosure.request_type.category
			cat_key = category.category_id
			if not cat_key in categories:
				categories[cat_key] = []
				serialized_category = category.serialize()
				serialized_category['disclosures'] = []
				categories[cat_key] = serialized_category
			categories[cat_key]['disclosures'].append(disclosure.serialize())
		return categories

	def toTable(self):
		headerRow = ['Category', 'Sub Category']
		rows = []
		colTotals = ['TOTALS', 'N/A']
		for index in range(len(self.disclosures)):
			# Add categories to first and second columns
			columns = [
				self.disclosures[index].request_type.category.name,
				self.disclosures[index].request_type.name
			]
			for j in range(len(self.disclosures[index].disclosure_responses)):
				#add header row
				if index == 0:
					headerRow.append(self.disclosures[index].disclosure_responses[j].response.name)
					#Add empty slot to start totals list items
					colTotals.append(0)
				#done adding header row

				columns.append(self.disclosures[index].disclosure_responses[j].count)

				#Add to totals: Account for the two category columns by adding 2 to the index
				colTotals[j+2] += self.disclosures[index].disclosure_responses[j].count
			rows.append(columns)

		rows.insert(0, headerRow)
		rows.append(colTotals)
		return rows

	def toCSV(self):
		rows = self.toTable()
		
		si = StringIO.StringIO()
		cw = csv.writer(si)
		cw.writerows(rows)
		return si




