class QueryBuilder:
    # Static variables
    base_url = "https://www.marriott.com/search/findHotels.mi?"
    destination_address_types = 'destinationAddress.types=locality,political&'
    is_internal_search = 'isInternalSearch=true&'
    vs_initial_request = 'vsInitialRequest=falsecorporateCode=&'
    search_type = 'searchType=InCity&'
    single_search_auto_suggest = 'singleSearchAutoSuggest=Unmatched&'
    missing_check_in_date_msg = 'missingcheckInDateMsg=Please+enter+a+check-in+date.&'
    is_hotels_near_me_clicked = 'is-hotelsnearme-clicked=false&'
    for_hotels_near_me = 'for-hotels-nearme=Near&'
    page_type = 'pageType=advanced&'
    missing_check_out_date_msg = 'missingcheckOutDateMsg=Please+enter+a+check-out+date.&'
    destination_address_country = 'destinationAddress.country=US&'
    collapse_accordian = 'collapseAccordian=is-hidden&'
    single_search = 'singleSearch=true&'
    is_transient = 'isTransient=true&'
    initial_request = 'initialRequest=false&'
    from_to_date = 'fromToDate=&'
    cluster_code = 'clusterCode=none&'
    ending_string = 'view=list#/1/'

    def build_query(self, records_per_page_value, destination_address_latitude_value, destination_address_longitude_value, destination_address_value, search_radius_value, destination_address_place_id_value, destination_address_address_value, destination_address_secondary_text_value, destination_address_city_value, destination_address_main_text_value, destination_address_website_value, destination_address_destination_value, from_to_date_submit_value, from_date_value, to_date_value, to_date_default_format_value, from_date_default_format_value, flexible_date_search_value, is_hide_flexible_date_calendar_value, t_start_value, t_end_value, length_of_stay_value, room_count_box_value, guest_count_box_value, num_adults_per_room_value, children_count_box_value, children_count_value):
        # Build the query string here
        fully_built_string = (
            self.base_url +
            self.destination_address_types +
            self.is_internal_search +
            self.vs_initial_request +
            self.search_type +
            self.single_search_auto_suggest +
            self.missing_check_in_date_msg +
            self.is_hotels_near_me_clicked +
            self.for_hotels_near_me +
            self.page_type +
            self.missing_check_out_date_msg +
            self.destination_address_country +
            self.collapse_accordian +
            self.single_search +
            self.is_transient +
            self.initial_request +
            self.from_to_date +
            self.cluster_code +
            'recordsPerPage=' + records_per_page_value + '&' +
            'destinationAddress.latitude=' + destination_address_latitude_value + '&' +
            'destinationAddress.longitude=' + destination_address_longitude_value + '&' +
            'destinationAddress.stateProvince=' + destination_address_value + '&' +
            'searchRadius=' + search_radius_value + '&' +
            'destinationAddress.placeId=' + destination_address_place_id_value + '&' +
            'destinationAddress.address=' + destination_address_address_value + '&' +
            'destinationAddress.secondaryText=' + destination_address_secondary_text_value + '&' +
            'destinationAddress.city=' + destination_address_city_value + '&' +
            'destinationAddress.mainText=' + destination_address_main_text_value + '&' +
            'destinationAddress.website=' + destination_address_website_value + '&' +
            'destinationAddress.destination=' + destination_address_destination_value + '&' +
            'fromToDate_submit=' + from_to_date_submit_value + '&' +
            'fromDate=' + from_date_value + '&' +
            'toDate=' + to_date_value + '&' +
            'toDateDefaultFormat=' + to_date_default_format_value + '&' +
            'fromDateDefaultFormat=' + from_date_default_format_value + '&' +
            'flexibleDateSearch=' + flexible_date_search_value + '&' +
            'isHideFlexibleDateCalendar=' + is_hide_flexible_date_calendar_value + '&' +
            't-start=' + t_start_value + '&' +
            't-end=' + t_end_value + '&' +
            'lengthOfStay=' + length_of_stay_value + '&' +
            'roomCountBox=' + room_count_box_value + '&' +
            'guestCountBox=' + guest_count_box_value + '&' +
            'numAdultsPerRoom=' + num_adults_per_room_value + '&' +
            'childrenCountBox=' + children_count_box_value + '&' +
            'childrenCount=' + children_count_value + '&' +
            self.ending_string
        )
        return fully_built_string

